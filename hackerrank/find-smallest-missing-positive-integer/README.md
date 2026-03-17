# Find Smallest Missing Positive Integer

**Platform:** HackerRank
**Link:** https://www.hackerrank.com/contests/software-engineer-prep-kit/challenges/find-smallest-missing-positive-integer

Given an array of integers, return the smallest positive integer (starting from 1) that does not appear in the array. The array may contain duplicates, negatives, and zeros.

---

## Pattern

- **Category:** Arrays / In-Place Sorting
- **Pattern:** Cyclic sort
- **Key idea:** Place each value `v` in the range `[1, n]` at index `v - 1` by swapping, then scan for the first position where `orderNumbers[i] != i + 1`.

---

## Approach

We use an in-place cyclic sort to rearrange the array so that each positive integer `v` (where `1 <= v <= n`) sits at index `v - 1`.

For each element at index `i`:

1. If the element is out of range (`<= 0` or `> n`) or already in its correct position, skip it.
2. If the target position already holds the correct value (duplicate detection), skip it.
3. Otherwise, swap the element to its target index `elem - 1` and repeat without advancing `i`.

After the sort, scan the array for the first index where `orderNumbers[i] != i + 1` and return `i + 1`. If all positions match, return `n + 1`.

---

## Complexity

- **Time:** `O(n)` — each element is swapped at most once to its correct position
- **Space:** `O(1)` — in-place rearrangement, no extra data structures
