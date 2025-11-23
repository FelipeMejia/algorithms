# Check If N and Its Double Exist

**Platform:** LeetCode  
**Link:** https://leetcode.com/problems/check-if-n-and-its-double-exist/

Given an array `arr` of integers, check if there exist two indices `i` and `j` such that:

- `i != j`
- `arr[i] == 2 * arr[j]`

Return `True` if such a pair exists, otherwise return `False`.

---

## Pattern

- **Category:** Arrays / Hashing
- **Pattern:** Hash set for constant-time lookup
- **Key idea:** While scanning the array, use a set to quickly check if we've already seen either the double or the half of the current number.

---

## Approach

We scan the array from left to right and maintain a set `seen` with all numbers we've processed so far.

For each `num` in `arr`:

1. Check if `2 * num` is already in `seen`  
   → This would mean there exists some previous `x` such that `x == 2 * num`.

2. If `num` is even, check if `num // 2` is in `seen`  
   → This would mean there exists some previous `x` such that `num == 2 * x`.

3. If either condition is true, we immediately return `True`.

4. Otherwise, add `num` to `seen` and continue.

If we finish the loop without finding such a pair, return `False`.

This works for positive numbers, negative numbers, and zero.  
Note that `0` is special because `0 == 2 * 0`, so a pair of zeros should return `True`.

---

## Complexity

- **Time:** `O(n)` — single pass through the array with `O(1)` average-time set lookups
- **Space:** `O(n)` — in the worst case, all elements are stored in the set

---

## Local Tests

Included test cases in `solution.py`:

1. `arr = [10, 2, 5, 3]`  
   → `True` (`10 == 2 * 5`)

2. `arr = [3, 1, 7, 11]`  
   → `False` (no such pair)

3. `arr = [0, 0]`  
   → `True` (`0 == 2 * 0`)

4. `arr = [-2, -4, 1]`  
   → `True` (`-4 == 2 * -2`)

5. `arr = [-3, -1, 2, 5]`  
   → `False`
