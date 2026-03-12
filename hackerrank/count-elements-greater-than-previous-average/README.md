# Count Elements Greater Than Previous Average

**Platform:** HackerRank
**Link:** https://www.hackerrank.com/contests/software-engineer-prep-kit/challenges/count-elements-greater-than-previous-average

Given an array of positive integers, return the number of elements that are strictly greater than the average of all previous elements. Skip the first element.

---

## Pattern

- **Category:** Arrays / Prefix Sum
- **Pattern:** Running average with cumulative sum
- **Key idea:** Maintain a running sum of all previously seen elements to compute the average on the fly, avoiding recalculation each iteration.

---

## Approach

We iterate through the array starting from index 1, keeping a running sum of all previously visited elements.

For each element at index `i`:

1. Check if `elem * i > running_sum` (equivalent to `elem > running_sum / i`, but avoids floating-point division).
2. If true, increment the count.
3. Add the current element to `running_sum` and continue.

Return the final count.

---

## Complexity

- **Time:** `O(n)` — single pass through the array
- **Space:** `O(1)` — only a running sum and a counter

---

## Local Tests

Included test cases in `solution.py`:

1. `arr = [1, 2, 3, 4, 5]`
   → `4` (every element after the first is greater than the average of all previous)

2. `arr = [5, 4, 3, 2, 1]`
   → `0` (no element is greater than the average of all previous)

3. `arr = [10]`
   → `0` (single element, nothing to compare)

4. `arr = [1, 1, 1, 1]`
   → `0` (no element is strictly greater than the average of equal values)
