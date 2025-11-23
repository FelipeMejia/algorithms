from typing import List


class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        seen: set[int] = set()
        for num in arr:
            if 2 * num in seen or (num % 2 == 0 and num // 2 in seen):
                return True
            seen.add(num)
        return False


def run_tests():
    solution = Solution()

    # Example 1
    arr = [10, 2, 5, 3]
    answer = solution.checkIfExist(arr)
    assert answer is True

    # Example 2
    arr = [3, 1, 7, 11]
    answer = solution.checkIfExist(arr)
    assert answer is False

    # Edge case: includes zero (0 and 0 → 0 == 2 * 0)
    arr = [0, 0]
    answer = solution.checkIfExist(arr)
    assert answer is True

    # Edge case: negatives
    arr = [-2, -4, 1]
    answer = solution.checkIfExist(arr)
    assert answer is True  # -4 == 2 * -2

    # Edge case: no pair even with mixed numbers
    arr = [-3, -1, 2, 5]
    answer = solution.checkIfExist(arr)
    assert answer is False

    print("All tests passed! ✅")


if __name__ == "__main__":
    run_tests()
