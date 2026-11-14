import java.io.ByteArrayInputStream;
import java.io.ByteArrayOutputStream;
import java.io.InputStream;
import java.io.PrintStream;
import java.lang.reflect.InvocationTargetException;
import java.lang.reflect.Method;
import java.nio.charset.StandardCharsets;

/**
 * Helpers for exercise tests. Compiled automatically alongside every exercise's tests by
 * {@code ccm test}.
 *
 * <pre>
 *   String out = TestUtil.runMain(Exercise.class, "5\n3\n");   // stdin "5\n3\n"
 *   assertEquals("8", out.strip());
 * </pre>
 */
public final class TestUtil {
    private TestUtil() {}

    /** Runs {@code cls.main(args)} with no input and returns everything it printed. */
    public static String runMain(Class<?> cls) {
        return runMain(cls, "");
    }

    /** Runs {@code cls.main(args)} with {@code input} as System.in and returns everything it printed. */
    public static String runMain(Class<?> cls, String input, String... args) {
        return capture(input, () -> {
            Method main;
            try {
                main = cls.getMethod("main", String[].class);
            } catch (NoSuchMethodException e) {
                throw new AssertionError(
                        cls.getSimpleName() + " needs a 'public static void main(String[] args)' method");
            }
            try {
                main.invoke(null, (Object) args);
            } catch (InvocationTargetException e) {
                Throwable cause = e.getCause();
                if (cause instanceof RuntimeException re) throw re;
                if (cause instanceof Error err) throw err;
                throw new RuntimeException(cause);
            } catch (IllegalAccessException e) {
                throw new AssertionError(cls.getSimpleName() + ".main must be public", e);
            }
        });
    }

    /** Runs {@code body} with {@code input} as System.in and returns everything printed to System.out. */
    public static String capture(String input, Runnable body) {
        PrintStream oldOut = System.out;
        InputStream oldIn = System.in;
        ByteArrayOutputStream buffer = new ByteArrayOutputStream();
        try (PrintStream out = new PrintStream(buffer, true, StandardCharsets.UTF_8)) {
            System.setOut(out);
            System.setIn(new ByteArrayInputStream(input.getBytes(StandardCharsets.UTF_8)));
            body.run();
        } finally {
            System.setOut(oldOut);
            System.setIn(oldIn);
        }
        return buffer.toString(StandardCharsets.UTF_8).replace("\r\n", "\n");
    }
}
