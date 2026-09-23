# Palindrome Permutation

**LeetCode Problem:** 266
**Language:** Python

## Problem

Given a string `s`, determine whether a permutation of the string can form a palindrome.

A palindrome is a string that reads the same forward and backward.

For example:

```text id="0k0d2h"
"level"
```

is a palindrome.

The characters of the given string can be rearranged in any order.

The task is to check whether at least one such arrangement can form a palindrome.

## Example

Input:

```text id="j1j5df"
s = "code"
```

The character counts are:

```text id="1l8c7d"
c → 1
o → 1
d → 1
e → 1
```

There are more than one characters with odd frequency.

So it cannot be rearranged into a palindrome.

Output:

```text id="6j23o4"
False
```

Another example:

```text id="g3n6o7"
s = "aab"
```

The characters can be rearranged as:

```text id="wq0y2b"
"aba"
```

So the output is:

```text id="v1f4lc"
True
```

## Approach

First, count how many times each character appears in the string.

For a palindrome:

* Every character should generally appear an even number of times.
* At most one character can have an odd frequency.

The odd-frequency character, if present, can be placed in the center of the palindrome.

For example:

```text id="6f3z2y"
a → 2
b → 2
c → 1
```

This can form:

```text id="xq4k7p"
abcba
```

Therefore, the string can be rearranged into a palindrome.

## Key Idea

The important condition is:

```text id="5w7l0c"
Number of characters with odd frequency <= 1
```

If there are two or more characters with odd frequencies, a palindrome cannot be formed.

## Complexity

* **Time:** O(n)
* **Space:** O(n)

Here, `n` is the length of the string.

The dictionary stores the frequency of each character.

## Key Learning

This problem helped me practice:

* Hash maps
* Frequency counting
* Strings
* Palindrome concepts
* Character manipulation
* Logical conditions

## Conclusion

The solution counts the frequency of every character and checks how many characters have an odd frequency. If at most one character has an odd count, the string can be rearranged into a palindrome.

**Author: T. Nandhini**
