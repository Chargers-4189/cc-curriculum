#!/usr/bin/env python3
"""Upload courses, lessons and homework from this repo to Charging Courses (chargingcourses.com).

Lessons, homework and check-ins are rebuilt with build.py and sent to the site through the LearnHouse API.
Pages that already match are skipped. Anything that isn't on the site yet (a new lesson, homework,
chapter, or a whole new course) is created, and its id is saved in tools/lms/ids.yaml.

    python3 tools/lms/publish.py --dry-run          # show what would change, upload nothing
    python3 tools/lms/publish.py                    # update + create everything in courses on the site
    python3 tools/lms/publish.py courses/02-object-oriented          # create or update one course
    python3 tools/lms/publish.py courses/01-fundamentals/05-loops    # one chapter
    python3 tools/lms/publish.py courses/01-fundamentals/05-loops/01-while-loops   # one lesson

A course that isn't on the site yet is only created when you name its folder, so a plain run never
makes a surprise course. New courses are created unpublished: look them over, then publish them
from the dashboard. New lessons and homework inside a course are published right away.

Names on the site: a course and chapter use the title in course.yaml / chapter.yaml, a lesson
uses its folder name ("02-for-loops" -> "For Loops"), homework uses "<title> (Homework)", and a
check-in uses its title. Check-ins (courses/<course>/check-ins/*.yaml) go right after the lesson
named in their `after:` line (and that lesson's homework), and are graded automatically.
You can rename anything on the site afterwards; publishing never changes names.

API token: Dashboard -> Developers -> API Access -> Create Token, with create, read and update
rights for courses, chapters, activities and assignments. Put it in .env at the top of the repo
as CC_API_TOKEN=lh_... (.env is in .gitignore, so it never gets committed), or in the
CC_API_TOKEN environment variable.

Edits made on the site: after every upload, the page's content is saved (as a fingerprint) in
tools/lms/published.json. If a page has changed on the site since then, it's skipped and the
changes are shown, so nothing done on the site gets overwritten. Copy those changes into the repo
(then it's "up to date" again), or pass --force to replace them with the repo version.

Safety checks (a page is skipped with a message, unless you pass --force):
  - the page's images are kept, so the number of images must match the markdown
  - a page that has a kind of block the markdown can't make (a video, an embed...) is left alone,
    so nothing added by hand on the site gets wiped out
"""
from __future__ import annotations

import argparse
import difflib
import hashlib
import json
import mimetypes
import os
import re
import sys
import time
import urllib.error
import urllib.request
import uuid
from pathlib import Path

import yaml

sys.path.insert(0, str(Path(__file__).parent))
import build  # noqa: E402

API = build.SITE + "/api/v1"
ROOT = build.ROOT
COURSES = ROOT / "courses"
IDS = build.IDS
NUM = re.compile(r"^\d{2}-")
SMALL_WORDS = {"a", "an", "and", "as", "at", "by", "for", "in", "of", "on", "or", "the", "to", "vs"}


# ------------------------------------------------------------------ colors ---

COLOR = sys.stdout.isatty() and not os.environ.get("NO_COLOR")


def paint(code: str, text: str) -> str:
    return f"\033[{code}m{text}\033[0m" if COLOR else text


def status_color(result: str) -> str:
    """Green = changed, yellow = would change, dim = nothing to do, red = needs you."""
    if result.startswith(("SKIPPED", "WARNING")):
        return "1;31"
    if result.startswith(("would", "filled")):
        return "33"
    if result.startswith(("updated", "created", "linked", "put ")):
        return "32"
    return "2"


COUNTS: dict[str, int] = {}


def show(kind: str, name: str, result: str) -> None:
    first, _, rest = result.partition("\n")
    COUNTS[status_color(first)] = COUNTS.get(status_color(first), 0) + 1
    label = f"{name}: " if name else ""
    print(f"{paint('36', f'{kind:8}')}  {label}{paint(status_color(first), first)}" + ("\n" + rest if rest else ""))


# ------------------------------------------------------------------- state ---
# A fingerprint of what each page looked like right after we last uploaded it.

STATE_FILE = Path(__file__).parent / "published.json"


def load_state() -> dict:
    try:
        return json.loads(STATE_FILE.read_text(encoding="utf-8"))
    except (FileNotFoundError, json.JSONDecodeError):
        return {}


STATE = load_state()


def fingerprint(obj) -> str:
    return hashlib.sha256(json.dumps(obj, sort_keys=True).encode()).hexdigest()[:16]


def remember(act: str, live) -> None:
    STATE[act] = fingerprint(live)
    STATE_FILE.write_text(json.dumps(dict(sorted(STATE.items())), indent=2) + "\n", encoding="utf-8")


CREATED: set[str] = set()  # pages made by this run


def edited_on_site(act: str, live) -> bool:
    """True if the page changed on the site since we last uploaded it (or we never uploaded it)."""
    return act not in CREATED and STATE.get(act) != fingerprint(live)


def page_text(doc) -> list[str]:
    """One line of plain text per block, for showing what changed."""
    lines = []
    for block in (doc or {}).get("content") or []:
        parts: list[str] = []
        walk(block, lambda n: parts.append(n.get("text", "") if n.get("type") == "text"
                                           else " " if n.get("type") in ("paragraph", "heading") else ""))
        if block.get("type") == "blockImage":
            parts = ["[image]"]
        elif block.get("type") in ("blockCode", "blockQuiz"):
            parts = [f"[{block['type']}]"]
        line = " ".join("".join(parts).split())
        if line:
            lines.append(line)
    return lines


def changes(old: list[str], new: list[str], limit: int = 8) -> str:
    """The lines that differ, - for the site version and + for the repo version."""
    out = []
    for d in difflib.unified_diff(old, new, lineterm="", n=0):
        if d.startswith(("---", "+++", "@@")):
            continue
        line = d[:160] + ("..." if len(d) > 160 else "")
        out.append("      " + paint("31" if d.startswith("-") else "32", line))
    more = f"\n      ... and {len(out) - limit} more" if len(out) > limit else ""
    return "\n".join(out[:limit]) + more


# --------------------------------------------------------------------- api ---

def token() -> str:
    t = os.environ.get("CC_API_TOKEN", "").strip()
    env = ROOT / ".env"
    if not t and env.exists():
        for line in env.read_text(encoding="utf-8").splitlines():
            key, _, value = line.partition("=")
            if key.strip() == "CC_API_TOKEN":
                t = value.strip().strip("'\"")
    if not t:
        sys.exit("No API token. Add CC_API_TOKEN=lh_... to .env (see --help).")
    return t


class Api:
    def __init__(self, tok: str):
        self.auth = {"Authorization": f"Bearer {tok}", "Accept": "application/json",
                     "User-Agent": "cc-curriculum-publish"}

    def call(self, method: str, path: str, body=None, form: dict | None = None):
        headers = dict(self.auth)
        data = None
        if form is not None:
            data, ctype = multipart(form)
            headers["Content-Type"] = ctype
        elif body is not None:
            data = json.dumps(body).encode()
            headers["Content-Type"] = "application/json"
        for _ in range(5):
            req = urllib.request.Request(API + path, data=data, method=method, headers=headers)
            try:
                with urllib.request.urlopen(req, timeout=120) as r:
                    raw = r.read()
                    return json.loads(raw) if raw else None
            except urllib.error.HTTPError as e:
                if e.code == 429:
                    time.sleep(int(e.headers.get("Retry-After") or 5))
                    continue
                detail = e.read().decode(errors="replace")[:300]
                raise SystemExit(f"{method} {path} -> {e.code}: {detail}") from None
        raise SystemExit(f"{method} {path}: still rate limited after 5 tries")

    def get(self, p):
        return self.call("GET", p)

    def put(self, p, b):
        return self.call("PUT", p, b)

    def post(self, p, b=None, form=None):
        return self.call("POST", p, b, form)


def multipart(fields: dict) -> tuple[bytes, str]:
    """fields: name -> str, or name -> Path (sent as a file)."""
    boundary = "----cc" + uuid.uuid4().hex
    out = bytearray()
    for name, value in fields.items():
        out += f"--{boundary}\r\n".encode()
        if isinstance(value, Path):
            ctype = mimetypes.guess_type(value.name)[0] or "application/octet-stream"
            out += (f'Content-Disposition: form-data; name="{name}"; filename="{value.name}"\r\n'
                    f"Content-Type: {ctype}\r\n\r\n").encode()
            out += value.read_bytes()
        else:
            out += f'Content-Disposition: form-data; name="{name}"\r\n\r\n{value}'.encode()
        out += b"\r\n"
    out += f"--{boundary}--\r\n".encode()
    return bytes(out), f"multipart/form-data; boundary={boundary}"


# ------------------------------------------------------------------- repo ---

def numbered(folder: Path, marker: str) -> list[Path]:
    return sorted(p for p in folder.iterdir() if p.is_dir() and NUM.match(p.name) and (p / marker).exists())


def read_yaml(path: Path) -> dict:
    return (yaml.safe_load(path.read_text(encoding="utf-8")) or {}) if path.exists() else {}


def lesson_title(folder: Path) -> str:
    words = NUM.sub("", folder.name).split("-")
    return " ".join(w if i and w in SMALL_WORDS else w[:1].upper() + w[1:] for i, w in enumerate(words))


def homework_of(lesson: Path) -> list[Path]:
    ex = lesson / "exercises"
    if not ex.is_dir():
        return []
    return [p for p in sorted(ex.iterdir())
            if (p / "prompt.md").exists() and build.front_matter(p / "prompt.md")[0].get("type") == "homework"]


def checkins_after(lesson: Path) -> list[Path]:
    """Check-ins (courses/<course>/check-ins/*.yaml) that go right after this lesson."""
    course = COURSES / key(lesson).split("/")[0]
    folder = course / "check-ins"
    if not folder.is_dir():
        return []
    return [f for f in sorted(folder.glob("*.yaml"))
            if str(build.read_checkin(f).get("after", "")).strip("/") == str(lesson.relative_to(course))]


def section(name: str) -> dict:
    """A section of ids.yaml, created if it's missing or empty."""
    if not isinstance(IDS.get(name), dict):
        IDS[name] = {}
    return IDS[name]


SECTION = {"lesson": "lessons", "homework": "homework", "checkin": "checkins"}


def id_key(kind: str, item: Path) -> str:
    return hw_name(item) if kind == "homework" else key(item)


def page_id(kind: str, item: Path) -> str | None:
    return (IDS.get(SECTION[kind]) or {}).get(id_key(kind, item))


def hw_name(ex: Path) -> str:
    return ex.name.split("-", 1)[1]


def key(path: Path) -> str:
    return str(path.relative_to(COURSES))


def write_ids() -> None:
    def block(name, comment, mapping):
        lines = [f"{name}:  # {comment}"] + [f"  {k}: {v}" for k, v in (mapping or {}).items()]
        return "\n".join(lines) + "\n"
    text = ("# Where each course, lesson and homework lives on Charging Courses (chargingcourses.com).\n"
            "# The ids are the last part of the page's address: /course/<course>/activity/<activity>\n"
            "# tools/lms/publish.py fills these in when it creates something on the site,\n"
            "# and tools/lms/build.py uses them to turn lesson links into Charging Courses links.\n\n"
            f"org: {IDS.get('org', 1)}  # organization id on Charging Courses\n\n"
            + block("courses", "course folder (under courses/) -> course", IDS.get("courses")) + "\n"
            + block("lessons", "lesson folder (under courses/) -> activity", dict(sorted((IDS.get("lessons") or {}).items()))) + "\n"
            + block("homework", "exercise name -> assignment activity", IDS.get("homework")) + "\n"
            + block("checkins", "check-in file (under courses/) -> assignment activity", IDS.get("checkins")))
    build.IDS_FILE.write_text(text, encoding="utf-8")


# ----------------------------------------------------------------- helpers ---

def walk(node, fn):
    if isinstance(node, dict):
        fn(node)
        for c in node.get("content") or []:
            walk(c, fn)


def node_types(doc) -> set[str]:
    out: set[str] = set()
    walk(doc, lambda n: out.add(n.get("type")))
    return out


def images(doc) -> list[dict]:
    out: list[dict] = []
    walk(doc, lambda n: out.append(n) if n.get("type") == "blockImage" else None)
    return out


def fill_images(node, imgs):
    """Swap build.py's __image placeholders for image blocks (in order)."""
    if isinstance(node, dict):
        if node.get("type") == "__image":
            return imgs[node["attrs"]["index"]]
        if "content" in node:
            node["content"] = [fill_images(c, imgs) for c in node["content"]]
    return node


def image_node(block: dict) -> dict:
    return {"type": "blockImage", "attrs": {
        "blockObject": block, "size": None, "alignment": "center", "unsplash_url": None,
        "unsplash_photographer_name": None, "unsplash_photographer_url": None, "unsplash_photo_url": None}}


def simple(name: str) -> str:
    """Names compared loosely: 'Welcome!' matches 'welcome', 'PlugNMeet' matches 'Plugnmeet'."""
    return re.sub(r"[^a-z0-9]+", " ", name.lower()).strip()


def image_note(src: str) -> dict:
    return {"type": "callout", "attrs": {"type": "warning", "dismissible": False}, "content": [
        {"type": "paragraph", "content": [{"type": "text", "text": f"Add image here: {src} (from the repo). "
                                           "Put the image right above this note, then delete the note."}]}]}


def same(a, b) -> bool:
    return json.dumps(a, sort_keys=True) == json.dumps(b, sort_keys=True)


def trimmed(doc: dict) -> dict:
    """The editor adds an empty paragraph at the end of a page; ignore it when comparing."""
    blocks = list(doc.get("content") or [])
    while blocks and blocks[-1] == {"type": "paragraph"}:
        blocks.pop()
    return {**doc, "content": blocks}


def covers(live, want) -> bool:
    """True if everything in `want` is already in `live` (extra keys the site adds are ignored)."""
    if isinstance(want, dict):
        return isinstance(live, dict) and all(covers(live.get(k), v) for k, v in want.items())
    return same(live, want)


# ------------------------------------------------------------------ create ---

class Creator:
    """Creates whatever in one course folder isn't on the site yet, then puts it in repo order."""

    def __init__(self, api: Api, course: Path, args):
        self.api, self.course, self.args = api, course, args
        self.log: list[str] = []
        self.made = False

    def say(self, what: str) -> None:
        self.log.append(("would create " if self.args.dry_run else "created ") + what)

    def run(self, lessons: list[Path]) -> list[str]:
        cid = (IDS.get("courses") or {}).get(self.course.name)
        if not cid:
            cid = self.create_course()
            if not cid:
                return self.log
        meta = self.api.get(f"/courses/course_{cid}/meta?with_unpublished_activities=true&slim=true")
        self.course_id, org = meta["id"], meta["org_id"]
        IDS.setdefault("org", org)
        chapters = {c["id"]: c for c in meta["chapters"]}
        act_chapter = {a["activity_uuid"].removeprefix("activity_"): c["id"]
                       for c in meta["chapters"] for a in c["activities"]}
        act_id = {a["activity_uuid"].removeprefix("activity_"): a["id"]
                  for c in meta["chapters"] for a in c["activities"]}
        order = [[c["id"], [a["id"] for a in c["activities"]]] for c in meta["chapters"]]

        repo_rank: dict[int, int] = {}  # site chapter -> position in the repo
        for ch_dir in numbered(self.course, "chapter.yaml"):
            ch_lessons = [l for l in numbered(ch_dir, "lecture.md") if l in lessons]
            if not ch_lessons:
                found = self.find_chapter(ch_dir, act_chapter, chapters)
                if found is not None:
                    repo_rank.setdefault(found, len(repo_rank))
                continue
            ch = self.find_chapter(ch_dir, act_chapter, chapters)
            if ch is None:
                ch = self.create_chapter(ch_dir, org)
                if ch is None:  # dry run
                    for l in ch_lessons:
                        self.say(f"lesson {key(l)}")
                        for h in homework_of(l):
                            self.say(f"homework {key(h)}")
                        for c in checkins_after(l):
                            self.say(f"check-in {key(c)}")
                    continue
                order.append([ch, []])
            repo_rank.setdefault(ch, len(repo_rank))
            acts = next(c[1] for c in order if c[0] == ch)
            prev_act = None
            for lesson in ch_lessons:
                items = ([("lesson", lesson)] + [("homework", h) for h in homework_of(lesson)]
                         + [("checkin", c) for c in checkins_after(lesson)])
                for kind, item in items:
                    uid = page_id(kind, item)
                    if uid and uid in act_id:
                        if act_chapter.get(uid) == ch:
                            prev_act = act_id[uid]
                        continue
                    if uid:  # in ids.yaml but gone from the site
                        self.log.append(f"WARNING: {key(item)} is in ids.yaml but its page isn't in this course")
                        continue
                    found = self.existing(item, kind, chapters[ch] if ch in chapters else None, act_id)
                    if found:
                        prev_act = act_id[found]
                        continue
                    new_id = (self.create_lesson(lesson, ch) if kind == "lesson"
                              else self.create_homework(item, ch, org) if kind == "homework"
                              else self.create_checkin(item, ch, org))
                    if new_id is None:
                        continue
                    acts.insert(acts.index(prev_act) + 1 if prev_act in acts else len(acts), new_id)
                    prev_act = new_id
        if self.made and not self.args.dry_run:
            # chapters from the repo go in repo order; chapters only on the site keep their spot
            slots = [i for i, c in enumerate(order) if c[0] in repo_rank]
            ranked = sorted((order[i] for i in slots), key=lambda c: repo_rank[c[0]])
            for i, c in zip(slots, ranked):
                order[i] = c
            self.api.put(f"/chapters/course/course_{cid}/order", {"chapter_order_by_ids": [
                {"chapter_id": c, "activities_order_by_ids": [{"activity_id": a} for a in acts]}
                for c, acts in order]})
            self.log.append("put everything in repo order")
        return self.log

    def existing(self, item: Path, kind: str, chapter: dict | None, act_id: dict) -> str | None:
        """A page already on the site with this lesson's name (made by hand): link it, don't duplicate it."""
        if not chapter:
            return None
        taken = {v for sec in SECTION.values() for v in (IDS.get(sec) or {}).values()}
        if kind == "lesson":
            names = {simple(lesson_title(item))}
        elif kind == "checkin":
            names = {simple(build.read_checkin(item)["title"])}
        else:
            title = build.front_matter(item / "prompt.md")[0].get("title") or hw_name(item)
            names = {simple(title), simple(f"{title} (Homework)")}
        for a in chapter["activities"]:
            uid = a["activity_uuid"].removeprefix("activity_")
            is_hw = a["activity_type"] == "TYPE_ASSIGNMENT"
            if uid not in taken and is_hw == (kind != "lesson") and simple(a["name"]) in names:
                section(SECTION[kind])[id_key(kind, item)] = uid
                self.log.append(f"{'would link' if self.args.dry_run else 'linked'} {key(item)} "
                                f"to the page already on the site called '{a['name']}'")
                if not self.args.dry_run:
                    write_ids()
                build.reload_ids() if not self.args.dry_run else None
                return uid
        return None

    def save(self) -> None:
        self.made = True
        write_ids()
        build.reload_ids()

    def create_course(self) -> str | None:
        meta = read_yaml(self.course / "course.yaml")
        name = meta.get("title") or lesson_title(self.course)
        self.say(f"course '{name}' (unpublished)")
        if self.args.dry_run:
            return None
        desc = meta.get("description") or ""
        org = IDS.get("org", 1)
        c = self.api.post(f"/courses/?org_id={org}", form={
            "name": name, "description": desc, "about": desc, "public": "true"})
        section("courses")[self.course.name] = c["course_uuid"].removeprefix("course_")
        self.save()
        return IDS["courses"][self.course.name]

    def find_chapter(self, ch_dir: Path, act_chapter: dict, chapters: dict) -> int | None:
        """The site chapter that already holds this folder's lessons, or one with the same name."""
        for l in numbered(ch_dir, "lecture.md"):
            uid = (IDS.get("lessons") or {}).get(key(l))
            if uid in act_chapter:
                return act_chapter[uid]
        title = read_yaml(ch_dir / "chapter.yaml").get("title") or lesson_title(ch_dir)
        return next((cid for cid, c in chapters.items() if c["name"] == title), None)

    def create_chapter(self, ch_dir: Path, org: int) -> int | None:
        meta = read_yaml(ch_dir / "chapter.yaml")
        name = meta.get("title") or lesson_title(ch_dir)
        self.say(f"chapter '{name}'")
        if self.args.dry_run:
            return None
        c = self.api.post("/chapters/", {"name": name, "description": meta.get("description") or "",
                                         "org_id": org, "course_id": self.course_id})
        self.made = True
        return c["id"]

    def create_lesson(self, lesson: Path, chapter: int) -> int | None:
        self.say(f"lesson {key(lesson)}")
        if self.args.dry_run:
            return None
        a = self.api.post("/activities/", {
            "name": lesson_title(lesson), "chapter_id": chapter, "activity_type": "TYPE_DYNAMIC",
            "activity_sub_type": "SUBTYPE_DYNAMIC_PAGE", "content": {"type": "doc", "content": []},
            "published": True})
        section("lessons")[key(lesson)] = a["activity_uuid"].removeprefix("activity_")
        CREATED.add(section("lessons")[key(lesson)])
        self.save()
        return a["id"]

    def create_homework(self, ex: Path, chapter: int, org: int) -> int | None:
        self.say(f"homework {key(ex)}")
        if self.args.dry_run:
            return None
        hw = build.build_homework(ex)
        a = self.create_assignment(f"{hw['title']} (Homework)", hw["assignment_description"], [hw["task"]],
                                   chapter, org, auto_grading=False)
        section("homework")[hw_name(ex)] = a["activity_uuid"].removeprefix("activity_")
        CREATED.add(section("homework")[hw_name(ex)])
        self.save()
        return a["id"]

    def create_checkin(self, path: Path, chapter: int, org: int) -> int | None:
        self.say(f"check-in {key(path)}")
        if self.args.dry_run:
            return None
        c = build.build_checkin(path)
        a = self.create_assignment(c["title"], c["assignment_description"], c["tasks"], chapter, org,
                                   auto_grading=True)
        section("checkins")[key(path)] = a["activity_uuid"].removeprefix("activity_")
        CREATED.add(section("checkins")[key(path)])
        self.save()
        return a["id"]

    def create_assignment(self, title: str, description: str, tasks: list[dict], chapter: int, org: int,
                          auto_grading: bool) -> dict:
        a = self.api.post("/activities/", {
            "name": title, "chapter_id": chapter, "activity_type": "TYPE_ASSIGNMENT",
            "activity_sub_type": "SUBTYPE_ASSIGNMENT_ANY", "content": {}, "published": True})
        asg = self.api.post("/assignments/", {
            "title": title, "description": description, "due_date": None,
            "grading_type": "PERCENTAGE", "ungraded": False, "auto_grading": auto_grading,
            "anti_copy_paste": False, "show_correct_answers": False, "allow_retries": False,
            "max_retries": 0, "org_id": org, "course_id": self.course_id, "chapter_id": chapter,
            "activity_id": a["id"]})
        for task in tasks:
            self.api.post(f"/assignments/{asg['assignment_uuid']}/tasks", task)
        self.api.put(f"/assignments/{asg['assignment_uuid']}", {"published": True})
        return a


# ----------------------------------------------------------------- publish ---

def publish_lesson(api: Api, folder: Path, act: str, args) -> str:
    built = build.build_lesson(folder)
    path = f"/activities/activity_{act}"
    live = (api.get(path) or {}).get("content") or {}
    imgs = images(live)
    need = len(built["images"])
    if need and not imgs and not (live.get("content") or []):
        # A brand-new, empty page. API tokens can't upload images, so mark where each one goes.
        if args.dry_run:
            return f"would fill in the page ({need} image(s) to add by hand after)"
        notes = [image_note(src) for src in built["images"]]
        api.put(path, {"content": fill_images(built["content"], notes)})
        remember(act, trimmed((api.get(path) or {}).get("content") or {}))
        return (f"filled in; now add {need} image(s) in the editor where the notes say "
                f"({', '.join(built['images'])}), then run this again")
    if need != len(imgs) and not args.force:
        if "Add image here:" in json.dumps(live):
            return (f"SKIPPED: waiting for images. Add {need} image(s) in the editor where the "
                    f"notes say (it has {len(imgs)} so far), then run this again")
        return f"SKIPPED: the page has {len(imgs)} image(s), the markdown has {need}"
    extra = node_types(live) - node_types(built["content"]) - {"blockImage", None}
    if extra and not args.force:
        return f"SKIPPED: the page has blocks the markdown doesn't make ({', '.join(sorted(extra))})"
    if need > len(imgs):
        return "SKIPPED: not enough images on the page to fill the markdown's images"
    content = fill_images(built["content"], imgs)
    if same(trimmed(content), trimmed(live)):
        if not args.dry_run and STATE.get(act) != fingerprint(trimmed(live)):
            remember(act, trimmed(live))
        return "up to date"
    diff = changes(page_text(live), page_text(content))
    if edited_on_site(act, trimmed(live)) and not args.force:
        why = ("it changed on the site since the last publish" if act in STATE
               else "it wasn't published from the repo before, so it may have site edits")
        return (f"SKIPPED: {why}. Copy the site's changes into the repo, or use --force to replace them "
                f"(- site, + repo):\n{diff}")
    if args.dry_run:
        return f"would update (- site, + repo):\n{diff}"
    api.put(path, {"content": content})
    remember(act, trimmed((api.get(path) or {}).get("content") or {}))
    return "updated"


def assignment_snapshot(api: Api, act: str) -> tuple[dict, list[dict], dict]:
    asg = api.get(f"/assignments/activity/activity_{act}")
    live = sorted(api.get(f"/assignments/{asg['assignment_uuid']}/tasks") or [], key=lambda t: t.get("order") or 0)
    snap = {"description": asg.get("description"),
            "tasks": [{k: t.get(k) for k in ("title", "description", "hint", "assignment_type", "contents",
                                              "max_grade_value")} for t in live]}
    return asg, live, snap


def sync_assignment(api: Api, act: str, description: str, tasks: list[dict], args) -> str:
    asg, live, snap = assignment_snapshot(api, act)
    a_uuid = asg["assignment_uuid"]
    if len(live) > len(tasks) and not args.force:
        return f"SKIPPED: the assignment has {len(live)} tasks, the repo has {len(tasks)}"
    up_to_date = asg.get("description") == description and len(live) == len(tasks) and \
        all(covers(live[i], want) for i, want in enumerate(tasks))
    if up_to_date:
        if not args.dry_run and STATE.get(act) != fingerprint(snap):
            remember(act, snap)
        return "up to date"
    if edited_on_site(act, snap) and not args.force:
        why = ("it changed on the site since the last publish" if act in STATE
               else "it wasn't published from the repo before, so it may have site edits")
        return f"SKIPPED: {why}. Copy the site's changes into the repo, or use --force to replace them."
    changes = []
    if asg.get("description") != description:
        changes.append("instructions")
        if not args.dry_run:
            api.put(f"/assignments/{a_uuid}", {"description": description})
    for i, want in enumerate(tasks):
        if i < len(live):
            if not covers(live[i], want):
                changes.append(f"task {i + 1}")
                if not args.dry_run:
                    api.put(f"/assignments/{a_uuid}/tasks/{live[i]['assignment_task_uuid']}", want)
        else:
            changes.append(f"new task {i + 1}")
            if not args.dry_run:
                api.post(f"/assignments/{a_uuid}/tasks", want)
    if not args.dry_run:
        remember(act, assignment_snapshot(api, act)[2])
    return ("would update " if args.dry_run else "updated ") + ", ".join(changes)


def publish_homework(api: Api, folder: Path, act: str, args) -> str:
    hw = build.build_homework(folder)
    return sync_assignment(api, act, hw["assignment_description"], [hw["task"]], args)


def publish_checkin(api: Api, path: Path, act: str, args) -> str:
    c = build.build_checkin(path)
    return sync_assignment(api, act, c["assignment_description"], c["tasks"], args)


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("paths", nargs="*", type=Path,
                    help="only these course / chapter / lesson / homework folders (default: every course on the site)")
    ap.add_argument("--dry-run", action="store_true", help="check what would change without uploading")
    ap.add_argument("--force", action="store_true", help="skip the safety checks")
    args = ap.parse_args()

    on_site = set(IDS.get("courses") or {})
    courses = numbered(COURSES, "course.yaml")
    wanted = [p.resolve() for p in args.paths]
    for p in wanted:
        if not p.is_dir() or COURSES not in p.parents:
            sys.exit(f"Not a folder under courses/: {p}")

    def under(path: Path) -> bool:  # path is one of the named folders, or inside one
        return not wanted or any(path == w or w in path.parents for w in wanted)

    plan: dict[Path, tuple[list[Path], list[Path], list[Path]]] = {}  # course -> (lessons, homework, check-ins)
    for course in courses:
        if wanted and not any(course == w or course in w.parents for w in wanted):
            continue
        if course.name not in on_site:
            if course not in wanted:
                if wanted:
                    sys.exit(f"{key(course)} isn't on the site yet. To create it, run: "
                             f"python3 tools/lms/publish.py courses/{course.name}")
                show("course", course.name, "not on the site (to create it: "
                     f"python3 tools/lms/publish.py courses/{course.name})")
                continue
        lessons, homework, checkins = [], [], []
        for ch in numbered(course, "chapter.yaml"):
            for lesson in numbered(ch, "lecture.md"):
                if under(lesson):
                    lessons.append(lesson)
                homework += [h for h in homework_of(lesson) if under(h)]
                checkins += [c for c in checkins_after(lesson) if under(c)]
        plan[course] = (lessons, homework, checkins)

    api = Api(token())
    problems = 0
    for course, (lessons, homework, checkins) in plan.items():
        # create anything missing (lessons named on their own still get their homework created)
        parents = {h.parent.parent for h in homework} | {course / build.read_checkin(c)["after"] for c in checkins}
        for line in Creator(api, course, args).run(sorted(set(lessons) | parents)):
            problems += line.startswith("WARNING")
            show("create", "", line)
        for kind, items, fn in (("lesson", lessons, publish_lesson), ("homework", homework, publish_homework),
                                ("checkin", checkins, publish_checkin)):
            for folder in items:
                act = page_id(kind, folder)
                if not act:
                    continue  # only happens on a dry run: it would be created above
                result = fn(api, folder, act, args)
                problems += result.startswith("SKIPPED")
                show(kind, key(folder), result)
    names = {"32": "changed", "33": "would change", "2": "up to date", "1;31": "need you"}
    print("\n" + "   ".join(paint(c, f"{COUNTS[c]} {n}") for c, n in names.items() if COUNTS.get(c)))
    if problems:
        print(paint("1;31", f"{problems} problem(s). Fix them, or rerun with --force if you're sure."))
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
