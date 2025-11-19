from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        """
        Removes all occurrences of val in-place from nums.
        Returns the number of elements not equal to val.
        """
        j = 0  # slow pointer: position to write next kept element
        for i in range(len(nums)):  # fast pointer: scans the array
            if nums[i] != val:
                nums[j] = nums[i]
                j += 1

        return j


def run_tests():
    solution = Solution()

    # Example 1
    nums = [3, 2, 2, 3]
    val = 3
    expected = [2, 2]
    k = solution.removeElement(nums, val)
    assert k == len(expected)
    assert sorted(nums[:k]) == sorted(expected)

    # Example 2
    nums = [0, 1, 2, 2, 3, 0, 4, 2]
    val = 2
    expected = [0, 1, 3, 0, 4]  # any order is fine
    k = solution.removeElement(nums, val)
    assert k == len(expected)
    assert sorted(nums[:k]) == sorted(expected)

    # Edge case: no elements equal to val
    nums = [1, 3, 5]
    val = 2
    expected = [1, 3, 5]
    k = solution.removeElement(nums, val)
    assert k == len(expected)
    assert nums[:k] == expected

    # Edge case: all elements equal to val
    nums = [4, 4, 4]
    val = 4
    expected = []
    k = solution.removeElement(nums, val)
    assert k == len(expected)
    assert nums[:k] == expected

    # Edge case: empty array
    nums = []
    val = 1
    expected = []
    k = solution.removeElement(nums, val)
    assert k == len(expected)
    assert nums[:k] == expected

    print("All tests passed! ✅")


if __name__ == "__main__":
    run_tests()
