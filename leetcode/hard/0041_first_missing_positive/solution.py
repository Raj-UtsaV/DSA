"""Canonical solution metadata.

Problem Number: 41
Problem Title: First Missing Positive
Platform: LeetCode
Difficulty: Hard
Official Platform Topics: Array, Hash Table
Study Tags: Cyclic placement
Canonical URL: https://leetcode.com/problems/first-missing-positive/
"""

"""
Problem Description:
--------------------
LeetCode 42. First Missing Positive
Link: https://leetcode.com/problems/first-missing-positive/

Given an unsorted integer array `nums`, return the smallest missing positive integer.
You must implement an algorithm that runs in O(n) time and uses constant extra space.

Example:
--------
Input: nums = [3, 4, -1, 1]
Output: 2

"""

#!IDEA
"""
The problem requires an O(n) time and O(1) space solution, which rules out simple sorting or using an extra hash set. The optimal approach uses the array itself as a hash map, a technique often called cyclic sort.

Optimal Approach (Cyclic Sort):
-------------------------------
The core idea is to place each number `x` in its "correct" position, which would be the index `x - 1`. For an array of size `n`, we are only concerned with positive integers from 1 to `n`. Any number outside this range (negative, zero, or > n) can be ignored.

1.  **Placement Phase**:
    - Iterate through the array from `i = 0` to `n-1`.
    - For each number `nums[i]`, check if it's a candidate for placement (i.e., `1 <= nums[i] <= n`).
    - If it is, and if it's not already in its correct spot (`nums[i] != nums[nums[i] - 1]`), swap it with the number at its correct index.
    - We use a `while` loop for this swapping process because the new number at `nums[i]` after a swap might also need to be moved.

2.  **Verification Phase**:
    - After the placement phase, the array should ideally look like `[1, 2, 3, ..., n]`, with some exceptions for numbers that were out of range.
    - Iterate through the modified array one last time.
    - The first index `i` where `nums[i]` is not equal to `i + 1` indicates that `i + 1` is the smallest missing positive number.

3.  **Edge Case**:
    - If the loop completes without finding any misplaced number, it means the array contains all numbers from 1 to `n`. In this case, the smallest missing positive is `n + 1`.

Alternative (Non-Optimal) Approaches:
- **Sorting**: Sort the array (O(n log n)) and iterate to find the first gap.
- **Hash Set**: Use a set (O(n) space) to store all numbers, then iterate from 1 upwards to find the first number not in the set.

"""

from typing import List

class Solution:
    # 1. Sort-based solution (O(n log n) time, O(1) space)
    def firstMissingPositive_sort(self, nums: List[int]) -> int:
        nums.sort()
        smallest = 1
        for num in nums:
            if num == smallest:
                smallest += 1
        return smallest

    # 2. O(n) time & O(n) space version
    def firstMissingPositive_space(self, nums: List[int]) -> int:
        n = len(nums)
        present = [False] * (n + 2)

        for num in nums:
            if 1 <= num <= n:
                present[num] = True

        for i in range(1, n + 2):
            if not present[i]:
                return i

    # 3. O(n) time & O(1) space version (optimal)
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)

        for i in range(n):
            while 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]:
                correct_index = nums[i] - 1
                nums[i], nums[correct_index] = nums[correct_index], nums[i]

        for i in range(n):
            if nums[i] != i + 1:
                return i + 1

        return n + 1

# --- Testing System ---
def test_solution(func, test_cases):
    for idx, (input_val, expected) in enumerate(test_cases, 1):
        # Make a copy to avoid modifying the original test case list
        input_copy = input_val[:]
        output = func(input_copy)
        if output == expected:
            print(f"Test case {idx}: ✅ Passed")
        else:
            print(f"Test case {idx}: ❌ Failed")
            print(f"  Input: {input_val}")
            print(f"  Output: {output}")
            print(f"  Expected: {expected}")

# --- Example Test Cases ---
if __name__ == "__main__":
    sol = Solution()
    test_cases = [
        ([1, 2, 0], 3),
        ([3, 4, -1, 1], 2),
        ([7, 8, 9, 11, 12], 1),
        ([0], 1),
        ([1], 2),
        ([2, 2, 2, 2], 1),
    ]

    print("--- Testing Optimal Solution (O(n) time, O(1) space) ---")
    test_solution(sol.firstMissingPositive, test_cases)

"""
Dry Run Example (Optimal Solution):
-----------------------------------
Input: nums = [3, 4, -1, 1] (n=4)

i = 0, nums[0] = 3. Correct index is 2. Swap nums[0] and nums[2].
   nums -> [-1, 4, 3, 1]
   (while loop continues for i=0) nums[0] = -1. Out of range [1,4]. Stop while.

i = 1, nums[1] = 4. Correct index is 3. Swap nums[1] and nums[3].
   nums -> [-1, 1, 3, 4]
   (while loop continues for i=1) nums[1] = 1. Correct index is 0. Swap nums[1] and nums[0].
   nums -> [1, -1, 3, 4]
   (while loop continues for i=1) nums[1] = -1. Out of range. Stop while.

i = 2, nums[2] = 3. Correct index is 2. nums[2] == nums[3-1]. Already correct.

i = 3, nums[3] = 4. Correct index is 3. nums[3] == nums[4-1]. Already correct.

Placement phase ends. Final array: [1, -1, 3, 4]

Verification phase:
- i = 0: nums[0] (1) == 0 + 1. OK.
- i = 1: nums[1] (-1) != 1 + 1. Mismatch!

Return i + 1, which is 1 + 1 = 2.
"""
