# Remove Element

**Platform:** LeetCode  
**Link:** https://leetcode.com/problems/remove-element/

Given an integer array `nums` and an integer `val`, remove all occurrences of `val` in-place.  
The order of the remaining elements may change.

You must:

1. Modify `nums` such that the first `k` elements are those that are **not** equal to `val`.
2. Return `k` — the number of elements not equal to `val`.
3. Anything beyond index `k` does not matter.

---

## Pattern

- **Category:** Arrays
- **Pattern:** Two Pointers (slow/fast) / In-place filter
- **Key idea:** Use one pointer to scan and another to overwrite the array with kept elements.

---

## Approach

Use two indices:

- `i`: fast pointer, iterates over every index in `nums`.
- `j`: slow pointer, tracks the position where the next kept element should be written.

Algorithm:

1. Initialize `j = 0`.
2. For each `i` from `0` to `len(nums) - 1`:
   - If `nums[i] != val`, copy `nums[i]` to `nums[j]` and increment `j`.
3. After the loop, `j` is the number of elements not equal to `val`.
4. The first `j` elements in `nums` are the filtered result.

This works because we only overwrite positions we've already processed and never need elements past `i`.

---

## Complexity

- **Time:** `O(n)` — single pass through the array
- **Space:** `O(1)` — in-place, no extra array

---

## Local Tests

Included test cases in `solution.py`:

1. `nums = [3,2,2,3], val = 3`  
   → `k = 2`, first `k` elements are `[2,2]`.

2. `nums = [0,1,2,2,3,0,4,2], val = 2`  
   → `k = 5`, first `k` elements contain `[0,1,3,0,4]` in any order.

3. No element equal to `val` (array unchanged, full length returned).

4. All elements equal to `val` (`k = 0`, nothing kept).

5. Empty array (`k = 0`).
