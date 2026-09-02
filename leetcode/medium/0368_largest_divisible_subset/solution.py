"""Canonical solution metadata.

Problem Number: 368
Problem Title: Largest Divisible Subset
Platform: LeetCode
Difficulty: Medium
Official Platform Topics: Array, Math, Dynamic Programming, Sorting
Study Tags: LIS-style reconstruction
Canonical URL: https://leetcode.com/problems/largest-divisible-subset/
"""

"""
Problem Description:
--------------------
[problem:] LeetCode 368. Largest Divisible Subset
[link:] https://leetcode.com/problems/largest-divisible-subset/
[description:] Given a set of distinct positive integers `nums`, return the largest subset `answer` such that for every pair `(answer[i], answer[j])` of elements in this subset, one of the following is true: `answer[i] % answer[j] == 0` or `answer[j] % answer[i] == 0`. If there are multiple solutions, return any of them.

Example:
--------
Input: nums = [1,2,3]
Output: [1,2]
Explanation: [1,3] is also accepted.

Input: nums = [1,2,4,8]
Output: [1,2,4,8]

"""

#!IDEA
"""
This problem can be solved using a dynamic programming approach that is very similar to the one used for finding the Longest Increasing Subsequence (LIS).

--- Solution 1: Dynamic Programming (LIS-based) ---

* Core Idea:
    1.  **Sort the array**: First, sort the input array `nums`. This is a critical step. If we sort the array, for any two numbers `a` and `b` in a valid subset where `a < b`, it must be that `b % a == 0`. This simplifies the divisibility check.
    2.  **Apply LIS logic**: After sorting, the problem transforms into finding the longest subsequence where each element is divisible by the previous one.

* State:
    - `dp[i]`: The length of the largest divisible subset that *ends* with the element `nums[i]`.
    - `parent[i]`: To reconstruct the actual subset, this array stores the index of the previous element in the largest divisible subset ending at `nums[i]`.

* Core Logic:
    - Initialize `dp` array of size `n` with all 1s (each element is a divisible subset of size 1).
    - Initialize `parent` array where `parent[i] = i`, indicating each element is its own predecessor initially.
    - Iterate through the sorted `nums` array from `i = 0` to `n-1`.
    - For each `i`, iterate through all previous elements `j` (from `0` to `i-1`).
    - If `nums[i] % nums[j] == 0`, it means `nums[i]` can extend the divisible subset ending at `nums[j]`.
    - If extending the subset at `j` gives a longer subset for `i` (i.e., `1 + dp[j] > dp[i]`), we update:
        - `dp[i] = 1 + dp[j]`
        - `parent[i] = j` (to remember that `nums[j]` comes before `nums[i]` in this path).

* Result:
    - After filling the `dp` array, the maximum value in `dp` gives the size of the largest divisible subset.
    - Find the index (`last_index`) where this maximum value occurs. This is the last element of our result subset.
    - Backtrack from `last_index` using the `parent` array to reconstruct the entire subset.

* Complexity:
    - Time complexity: O(N^2) due to the nested loops. Sorting takes O(N log N). Total is dominated by O(N^2).
    - Space complexity: O(N) for the `dp` and `parent` arrays.
"""

from typing import List

class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        n = len(nums)
        if n == 0:
            return []

        nums.sort()
        dp = [1]*n
        parent = list(range(n))
        max_len = 1
        last_index = 0

        for i in range(n):
            for prev_index in range(i):
                if nums[i] % nums[prev_index] == 0 and 1 + dp[prev_index] > dp[i]:
                    dp[i] = 1 + dp[prev_index]
                    parent[i] = prev_index

            if dp[i] > max_len:
                max_len = dp[i]
                last_index = i

        # Reconstruct the subset by backtracking from the last_index
        subset = []
        while parent[last_index] != last_index:
            subset.append(nums[last_index])
            last_index = parent[last_index]
        subset.append(nums[last_index])

        return subset[::-1] # Reverse to get the correct order

# --- Testing System ---
def test_solution(func, test_cases):
    for idx, (input_val, expected_options) in enumerate(test_cases, 1):
        output = func(input_val)
        # Sort output to compare with sorted expected options
        output.sort()

        # Check if the output matches any of the valid expected options
        passed = any(output == sorted(opt) for opt in expected_options)

        if passed:
            print(f"Test case {idx}: ✅ Passed")
        else:
            print(f"Test case {idx}: ❌ Failed")
            print(f"  Input: {input_val}")
            print(f"  Output: {output}")
            print(f"  Expected one of: {expected_options}")

# --- Example Test Cases ---
if __name__ == "__main__":
    sol = Solution()
    test_cases = [
        ([1, 2, 3], [[1, 2], [1, 3]]),
        ([1, 2, 4, 8], [[1, 2, 4, 8]]),
        ([4, 8, 10, 240], [[4, 8, 240]]),
        ([1], [[1]]),
        ([], [[]]),
    ]

    test_solution(sol.largestDivisibleSubset, test_cases)

"""
Dry Run Example:
---------------
Input: nums = [1, 2, 4, 8] (already sorted)
n = 4

Initialize:
dp = [1, 1, 1, 1]
parent = [0, 1, 2, 3]
max_len = 1, last_index = 0

i = 0 (num=1): No prev_index. dp=[1,1,1,1], parent=[0,1,2,3]

i = 1 (num=2):
  prev_index = 0 (num=1): 2%1==0. 1+dp[0]>dp[1] (2>1).
    dp[1]=2, parent[1]=0.
    max_len=2, last_index=1.
  dp=[1,2,1,1], parent=[0,0,2,3]

i = 2 (num=4):
  prev_index = 0 (num=1): 4%1==0. 1+dp[0]>dp[2] (2>1).
    dp[2]=2, parent[2]=0.
  prev_index = 1 (num=2): 4%2==0. 1+dp[1]>dp[2] (3>2).
    dp[2]=3, parent[2]=1.
    max_len=3, last_index=2.
  dp=[1,2,3,1], parent=[0,0,1,3]

i = 3 (num=8):
  prev_index = 0 (num=1): 8%1==0. 1+dp[0]>dp[3] (2>1).
    dp[3]=2, parent[3]=0.
  prev_index = 1 (num=2): 8%2==0. 1+dp[1]>dp[3] (3>2).
    dp[3]=3, parent[3]=1.
  prev_index = 2 (num=4): 8%4==0. 1+dp[2]>dp[3] (4>3).
    dp[3]=4, parent[3]=2.
    max_len=4, last_index=3.
  dp=[1,2,3,4], parent=[0,0,1,2]

Final State:
dp = [1, 2, 3, 4]
parent = [0, 0, 1, 2]
max_len = 4, last_index = 3

Reconstruction:
- Start with last_index = 3. subset = []
- subset.append(nums[3]=8). last_index = parent[3] = 2. subset=[8]
- subset.append(nums[2]=4). last_index = parent[2] = 1. subset=[8,4]
- subset.append(nums[1]=2). last_index = parent[1] = 0. subset=[8,4,2]
- subset.append(nums[0]=1). last_index = parent[0] = 0. Loop terminates. subset=[8,4,2,1]

Return subset[::-1] -> [1, 2, 4, 8]
"""
