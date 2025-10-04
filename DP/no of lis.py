"""
Problem Description:
--------------------
[problem:] LeetCode 673. Number of Longest Increasing Subsequence
[link:] https://leetcode.com/problems/number-of-longest-increasing-subsequence/
[description:] Given an integer array `nums`, return the number of longest increasing subsequences.
Notice that the sequence has to be strictly increasing.

Example:
--------
Input: nums = [1,3,5,4,7]
Output: 2
Explanation: The two longest increasing subsequences are [1, 3, 4, 7] and [1, 3, 5, 7].

Input: nums = [2,2,2,2,2]
Output: 5
Explanation: The length of the longest increasing subsequence is 1, and there are 5 subsequences of length 1, so output 5.

"""

#!IDEA
"""
This problem is an extension of the classic Longest Increasing Subsequence (LIS) problem. In addition to finding the length of the LIS, we also need to count how many such subsequences exist. We can solve this using a dynamic programming approach.

--- Solution: Dynamic Programming ---

* State:
    - `dp[i]`: The length of the longest increasing subsequence that *ends* at index `i`.
    - `cnt[i]`: The number of longest increasing subsequences that *end* at index `i`.

* Core Logic:
    1.  **Initialization**:
        - Initialize `dp` array of size `n` with all 1s. Every element by itself is an increasing subsequence of length 1.
        - Initialize `cnt` array of size `n` with all 1s. For each element, there is initially one way to form a subsequence of length 1 (the element itself).

    2.  **DP Calculation**:
        - Iterate through the `nums` array from `i = 0` to `n-1`.
        - For each `i`, iterate through all previous elements `j` (from `0` to `i-1`).
        - If `nums[i] > nums[j]`, it means `nums[i]` can extend the increasing subsequence ending at `nums[j]`.
            - **Case 1: Found a longer LIS**: If `dp[j] + 1 > dp[i]`, it means we've found a new, longer LIS ending at `i`. We update the length `dp[i] = dp[j] + 1` and reset the count `cnt[i]` to be the same as `cnt[j]`, because all the ways to form the LIS ending at `j` can now be extended to `i`.
            - **Case 2: Found another LIS of the same length**: If `dp[j] + 1 == dp[i]`, it means we've found another way to form an LIS of the current maximum length ending at `i`. We don't change `dp[i]`, but we add the counts from `cnt[j]` to `cnt[i]`.

* Result:
    1.  After filling the `dp` and `cnt` arrays, find the maximum value in the `dp` array. This is the length of the overall LIS (`max_len`).
    2.  Iterate through the `dp` array again. Sum up the `cnt[i]` for all indices `i` where `dp[i]` is equal to `max_len`. This sum is the total number of longest increasing subsequences.

* Complexity:
    - Time complexity: O(N^2) due to the nested loops.
    - Space complexity: O(N) for the `dp` and `cnt` arrays.
"""

from typing import List

class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 1:
            return n
        
        dp = [1]*n
        cnt = [1]*n
        max_len = 1

        for i in range(n):
            for j in range(i):
                if nums[i] > nums[j] and dp[j]+1 > dp[i]:
                    # Found a new longer LIS ending at i
                    dp[i] = dp[j]+1
                    cnt[i] = cnt[j]
                elif nums[i] > nums[j] and dp[j]+1 == dp[i]:
                    # Found another LIS of the same max length ending at i
                    cnt[i] += cnt[j]
            max_len = max(max_len, dp[i])

        count = 0
        for i in range(n):
            if dp[i] == max_len:
                count += cnt[i]
        return count

# --- Testing System ---
def test_solution(func, test_cases):
    for idx, (input_val, expected) in enumerate(test_cases, 1):
        output = func(input_val)
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
        ([1,3,5,4,7], 2),
        ([2,2,2,2,2], 5),
        ([1,2,4,3,5,4,7,2], 3),
        ([1], 1),
        ([], 0)
    ]
    
    test_solution(sol.findNumberOfLIS, test_cases)

"""
Dry Run Example:
---------------
Input: nums = [1, 3, 5, 4, 7]
n = 5

Initialize:
dp = [1, 1, 1, 1, 1]
cnt = [1, 1, 1, 1, 1]
max_len = 1

i = 0 (num=1): No prev elements. dp=[1,1,1,1,1], cnt=[1,1,1,1,1], max_len=1

i = 1 (num=3):
  j=0 (num=1): 3>1. dp[0]+1 > dp[1] (2>1). Update: dp[1]=2, cnt[1]=cnt[0]=1.
  dp=[1,2,1,1,1], cnt=[1,1,1,1,1], max_len=2

i = 2 (num=5):
  j=0 (num=1): 5>1. dp[0]+1 > dp[2] (2>1). Update: dp[2]=2, cnt[2]=cnt[0]=1.
  j=1 (num=3): 5>3. dp[1]+1 > dp[2] (3>2). Update: dp[2]=3, cnt[2]=cnt[1]=1.
  dp=[1,2,3,1,1], cnt=[1,1,1,1,1], max_len=3

i = 3 (num=4):
  j=0 (num=1): 4>1. dp[0]+1 > dp[3] (2>1). Update: dp[3]=2, cnt[3]=cnt[0]=1.
  j=1 (num=3): 4>3. dp[1]+1 > dp[3] (3>2). Update: dp[3]=3, cnt[3]=cnt[1]=1.
  j=2 (num=5): 4>5 is false.
  dp=[1,2,3,3,1], cnt=[1,1,1,1,1], max_len=3

i = 4 (num=7):
  j=0 (num=1): 7>1. dp[0]+1 > dp[4] (2>1). Update: dp[4]=2, cnt[4]=cnt[0]=1.
  j=1 (num=3): 7>3. dp[1]+1 > dp[4] (3>2). Update: dp[4]=3, cnt[4]=cnt[1]=1.
  j=2 (num=5): 7>5. dp[2]+1 > dp[4] (4>3). Update: dp[4]=4, cnt[4]=cnt[2]=1.
  j=3 (num=4): 7>4. dp[3]+1 == dp[4] (4==4). Same length, add counts: cnt[4] += cnt[3] -> cnt[4]=1+1=2.
  dp=[1,2,3,3,4], cnt=[1,1,1,1,2], max_len=4

Final Calculation:
max_len = 4.
Find all i where dp[i] == 4. Only at i=4.
count = cnt[4] = 2.

✅ Final Answer: 2
"""