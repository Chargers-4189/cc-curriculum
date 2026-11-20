## When Arrays Aren't Enough

- Ask: how big should the array be if we're reading names until someone types done?
- ArrayList is a class from the Java library. Same idea as Scanner: import it, make one, call methods

## Making an ArrayList

- `<String>` is what it holds. Don't go deep on generics, just "a list of Strings"
- Starts at size 0, no size needed

## Adding and Getting

- add, get, size. Print the list to see the brackets
- `add(1, "battery")`: everything after moves down

## Changing and Removing

- set vs add(index, ...): set replaces, add inserts
- remove by value and by index. No null holes, it shifts
- Try get(5) for the crash

## Searching

- contains, indexOf (-1 if missing), isEmpty. Compare to writing these loops by hand with an array

## Looping (spend time here)

- Regular for loop with size()/get(i), then the for-each loop (they saw it with arrays in the last lesson)
- For-each works on arrays too
- Removing while looping forward skips items. Act it out on the board with [4, -2, -7, 5]. Backward loop fixes it (that's practice 2)

## ArrayLists of Objects

- ArrayList<Robot> holds references, same as Robot[]

## Primitives Need Wrappers

- ArrayList<int> won't compile. Integer, Double, Boolean, Character
- remove(1) on a list of Integers removes index 1. Show it

## Arrays vs ArrayLists

- Go through the table. Fixed and known size: array. Changes while running: ArrayList
