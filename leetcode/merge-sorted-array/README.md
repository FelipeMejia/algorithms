# Merge Sorted Array

**Platform:** LeetCode  
**Link:** https://leetcode.com/problems/merge-sorted-array/

You are given two sorted integer arrays `nums1` and `nums2`, and two integers `m` and `n` representing the number of valid elements in each array.  
`nums1` has a size of `m + n`, where the last `n` positions are `0` placeholders.

The task is to **merge `nums2` into `nums1` in-place**, so that `nums1` becomes a single sorted array in non-decreasing order.

---

## Pattern

- **Category:** Arrays
- **Pattern:** Two Pointers (from the end)
- **Key idea:** Fill `nums1` from the back to avoid overwriting still-unprocessed values.

---

## Approach

Use three pointers:

- `i = m - 1` → last valid element in `nums1`
- `j = n - 1` → last element in `nums2`
- `k = m + n - 1` → last index in `nums1` (final merged position)

While `j >= 0`:

1. Compare `nums1[i]` and `nums2[j]`.
2. Place the larger one at `nums1[k]`.
3. Move the corresponding pointer (`i` or `j`) one step left.
4. Move `k` one step left.

If `i` becomes negative, copy the remaining elements from `nums2` into `nums1`.  
If `j` becomes negative, we are done (remaining `nums1` elements are already in place).

---

## Complexity

- **Time:** `O(m + n)`
- **Space:** `O(1)` (in-place)

---

## Local Tests

Included test cases in `solution.py`:

1. `nums1 = [1,2,3,0,0,0], m = 3; nums2 = [2,5,6], n = 3`  
   → `nums1` becomes `[1,2,2,3,5,6]`

2. `nums1 = [1], m = 1; nums2 = [], n = 0`  
   → `nums1` remains `[1]`

3. `nums1 = [0], m = 0; nums2 = [1], n = 1`  
   → `nums1` becomes `[1]`
