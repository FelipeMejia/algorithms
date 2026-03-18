# Check Palindrome by Filtering Non-Letters

**Platform:** HackerRank
**Link:** https://www.hackerrank.com/contests/software-engineer-prep-kit/challenges/check-palindrome-filter-non-letters/

Given a string containing letters, digits, and symbols, determine if it reads the same forwards and backwards when considering only alphabetic characters (case-insensitive).

---

## Pattern

- **Category:** Strings / Two Pointers
- **Pattern:** Two pointers
- **Key idea:** Filter out non-alphabetic characters, normalize case, then compare the resulting sequence from both ends moving inward.

---

## Approach

1. Iterate through the string and collect only alphabetic characters, converting each to lowercase.
2. If the filtered list is empty or has a single character, it is trivially a palindrome.
3. Use two pointers (`i` from the start, `j` from the end) to compare characters moving inward. If any pair mismatches, return `False`.

---

## Complexity

- **Time:** `O(n)` — single pass to filter characters, single pass to compare
- **Space:** `O(n)` — stores the filtered list of alphabetic characters
