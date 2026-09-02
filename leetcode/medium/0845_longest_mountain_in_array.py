"""Canonical solution metadata.

Problem Number: 845
Problem Title: Longest Mountain in Array
Platform: LeetCode
Difficulty: Medium
Official Platform Topics: Array, Two Pointers, Dynamic Programming, Enumeration
Study Tags: Increasing and decreasing runs
Canonical URL: https://leetcode.com/problems/longest-mountain-in-array/
"""

"""
Problem Description:
--------------------
[problem:] LeetCode 845. Longest Mountain in Array
[link:] https://leetcode.com/problems/longest-mountain-in-array/
[description:] You are given an integer array `nums`. A mountain subarray is a subarray `B` such that:
- `B.length >= 3`
- There exists some `i` with `0 < i < B.length - 1` such that `B[0] < B[1] < ... < B[i-1] < B[i] > B[i+1] > ... > B[B.length - 1]`

Return the length of the longest mountain subarray. If there is no mountain, return 0.

Example:
--------
Input: nums = [2,1,4,7,3,2,5]
Output: 5
Explanation: The longest mountain is [1,4,7,3,2] which has length 5.

Input: nums = [2,2,2]
Output: 0
Explanation: There is no mountain.

"""

#!IDEA
"""
The problem asks for the length of the longest subarray that first strictly increases and then strictly decreases.

--- Solution 1: Dynamic Programming (Bitonic Subsequence based) ---
This approach treats each index `i` as a potential peak of a mountain. For each peak, we find the length of the longest increasing sequence ending at `i` and the length of the longest decreasing sequence starting at `i`.

* State:
    - `dp_lis[i]`: The length of the longest increasing subarray ending at index `i`.
    - `dp_lds[i]`: The length of the longest decreasing subarray starting at index `i`.

* Core Logic:
    1.  **Calculate `dp_lis`**: Iterate from left to right. If `nums[i] > nums[i-1]`, then the increasing subarray at `i-1` can be extended. So, `dp_lis[i] = dp_lis[i-1] + 1`. Otherwise, a new increasing subarray of length 1 starts at `i`.
    2.  **Calculate `dp_lds`**: Iterate from right to left. If `nums[i] > nums[i+1]`, then the decreasing subarray at `i+1` can be extended. So, `dp_lds[i] = dp_lds[i+1] + 1`. Otherwise, a new decreasing subarray of length 1 starts at `i`.
    3.  **Find Longest Mountain**: Iterate through the array. For each index `i`, if it's a valid peak (meaning `dp_lis[i] > 1` and `dp_lds[i] > 1`), the length of the mountain is `dp_lis[i] + dp_lds[i] - 1`. The `-1` is because the peak element `nums[i]` is counted in both sequences. We track the maximum length found.

* Complexity:
    - Time complexity: O(N) for three separate passes over the array.
    - Space complexity: O(N) for the two DP arrays.

--- Solution 2: Single Pass (Two Pointers) ---
This is a more space-efficient approach that finds mountains in a single pass.

* State:
    - `base`: A pointer that marks the start of a potential mountain.
    - `end`: A pointer that scans ahead to find the peak and the end of the mountain.

* Core Logic:
    - Iterate through the array with `base` from `0` to `n-2`.
    - At each `base`, check if a potential uphill starts (`nums[base] < nums[base+1]`).
    - If an uphill starts:
        1.  **Find the peak**: Move `end` forward as long as `nums[end] < nums[end+1]`. The peak is at `end`.
        2.  **Check for a valid peak**: If `end` is still at `base` (no uphill found), continue.
        3.  **Find the end of the mountain**: Move `end` further as long as `nums[end] > nums[end+1]`.
        4.  **Calculate length**: If a downhill part was found, a valid mountain exists from `base` to `end`. Calculate its length (`end - base + 1`) and update the maximum.
        5.  **Update base**: Move `base` to `end` to start searching for the next mountain.
    - If no uphill starts at `base`, just move `base` to the next position.

* Complexity:
    - Time complexity: O(N). Although there's a nested loop structure, each element is visited at most twice (once by `base`, once by `end`).
    - Space complexity: O(1).
"""

from typing import List

class Solution:
    # Solution 1: Dynamic Programming (O(N) time, O(N) space)
    def longestMountain_dp(self, nums: List[int]) -> int:
        n = len(nums)

        dp_lis = [1] * n
        for i in range(1, n):
            if nums[i] > nums[i-1]:
                dp_lis[i] = dp_lis[i-1] + 1

        dp_lds = [1] * n
        for i in range(n-2, -1, -1):
            if nums[i] > nums[i+1]:
                dp_lds[i] = dp_lds[i+1] + 1

        ans = 0
        for i in range(n):
            # A mountain must have a strict uphill and downhill part
            if dp_lis[i] > 1 and dp_lds[i] > 1:
                ans = max(ans, dp_lis[i] + dp_lds[i] - 1)

        return ans

    # Solution 1 extended
    def longestMountain_dp_optmized(self, nums: List[int]) -> int:
        n = len(nums)
        dp_LIS = [1]*n
        dp_LDS = [1]*n

        for i in range(1,n):
            if nums[i] > nums[i-1]:
                dp_LIS[i] = dp_LIS[i-1]+1

        for i in range(n-2,-1,-1):
            if nums[i] > nums[i+1]:
                dp_LDS[i] = dp_LDS[i+1]+1

        ans = 0
        for i in range(n):
            if dp_LDS[i] > 1 and dp_LIS[i]>1:
                ans = max(dp_LDS[i]+dp_LIS[i]-1,ans)

        return ans


    # Solution 2: Single Pass (O(N) time, O(1) space)
    def longestMountain(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        base = 0
        while base < n:
            end = base
            # Find uphill part
            if end + 1 < n and nums[end] < nums[end+1]:
                while end + 1 < n and nums[end] < nums[end+1]:
                    end += 1

                # Check if a peak was found and there is a downhill part
                if end + 1 < n and nums[end] > nums[end+1]:
                    while end + 1 < n and nums[end] > nums[end+1]:
                        end += 1
                    # Update max length
                    ans = max(ans, end - base + 1)

            # Move base to the end of the processed section
            base = max(end, base + 1)

        return ans

# --- Testing System ---
def test_solution(func, test_cases):
    for idx, (input_val, expected) in enumerate(test_cases, 1):
        output = func(input_val)
        if output == expected:
            print(f"Test case {idx} ({func.__name__}): ✅ Passed")
        else:
            print(f"Test case {idx} ({func.__name__}): ❌ Failed")
            print(f"  Input: {input_val}")
            print(f"  Output: {output}")
            print(f"  Expected: {expected}")

# --- Example Test Cases ---
if __name__ == "__main__":
    sol = Solution()
    test_cases = [
        ([2,1,4,7,3,2,5], 5),
        ([2,2,2], 0),
        ([1,2,3,4,5], 0),
        ([5,4,3,2,1], 0),
        ([1,2,1,2,3,2,1], 5),
        ([875,884,239,731,723,685], 4)
    ]

    print("--- Testing DP Solution ---")
    test_solution(sol.longestMountain_dp, test_cases)
    print("--- Testing DP Optmized Solution ---")
    test_solution(sol.longestMountain_dp_optmized, test_cases)
    print("\n--- Testing Single Pass Solution ---")
    test_solution(sol.longestMountain, test_cases)
