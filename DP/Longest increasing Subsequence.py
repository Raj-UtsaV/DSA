"""
Problem Description:
--------------------
[problem:] LeetCode 300. Longest Increasing Subsequence
[link:] https://leetcode.com/problems/longest-increasing-subsequence/
[description:] Given an integer array `nums`, return the length of the longest strictly increasing subsequence.
A subsequence is a sequence that can be derived from an array by deleting some or no elements without changing the order of the remaining elements.

Example:
--------
Input: nums = [10,9,2,5,3,7,101,18]
Output: 4
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.

Input: nums = [0,1,0,3,2,3]
Output: 4

"""

#!IDEA
"""
This problem can be solved using several dynamic programming approaches.
The first set of solutions (recursion, 2D tabulation) uses a state based on the current index and the previous index, leading to an O(N^2) complexity. A more common O(N^2) approach uses a 1D DP array. The most optimal solution uses a clever trick with binary search to achieve O(N log N).

--- Solution 1: Memoized Recursion (Top-Down DP) ---
We define a recursive function `solve(i, prev_index)` that computes the length of the LIS from index `i` onwards, given that the previous element included in the LIS was at `prev_index`.

* State:
    - `i`: The current index in the `nums` array we are considering.
    - `prev_index`: The index of the last element added to our subsequence. We use -1 to indicate that no element has been chosen yet.

* Base Case:
    - If `i` reaches the end of the array (`i == n`), we can't add any more elements, so we return a length of 0.

* Core Logic (Choices at index `i`):
    - Don't Take `nums[i]`: We skip the current element and find the LIS from the rest of the array. The length is `solve(i + 1, prev_index)`.
    - Take `nums[i]`: We can only take `nums[i]` if it's greater than the previous element (`nums[prev_index]`). If `prev_index` is -1 (i.e., we are starting a new subsequence), we can always take `nums[i]`. If we take it, the length becomes `1 + solve(i + 1, i)`.
    
* Result:
    - The result for the state `(i, prev_index)` is the maximum of the "take" and "don't take" options.

* Optimization:
    - To avoid re-computation, we use a 2D DP table `dp[i][prev_index + 1]` to store the results. We use `prev_index + 1` because array indices can't be -1.

* Complexity:
    - Time: O(N^2) because there are N * (N+1) states.
    - Space: O(N^2) for the DP table + O(N) for recursion stack.

--- Solution 2: Tabulation (Bottom-Up DP) - Classic 1D DP ---
This is a more common and intuitive O(N^2) DP approach.

* State:
    - `dp[i]`: The length of the longest increasing subsequence that *ends* at index `i`.

* Core Logic:
    - Initialize a `dp` array of size `n` with all 1s, because every element by itself is an increasing subsequence of length 1.
    - We iterate through the array from `i = 1` to `n-1`.
    - For each `i`, we look back at all previous elements `j` (from `0` to `i-1`).
    - If `nums[i] > nums[j]`, it means we can potentially extend the increasing subsequence ending at `j` by including `nums[i]`. 
        ie if the j one is ending at 2 and the current is 3 then we can add it there and extend the list
    - The new length would be `dp[j] + 1`. We update `dp[i]` to be the maximum of its current value and `dp[j] + 1`.
    - `dp[i] = max(dp[i], 1 + dp[j])` for all `j < i` where `nums[i] > nums[j]`.

* Result:
    - The length of the LIS for the entire array is the maximum value in the `dp` array, as the LIS can end at any index.

* Complexity:
    - Time: O(N^2) due to the nested loops.
    - Space: O(N) for the `dp` array.

--- Solution 3: Optimized DP with Binary Search ---
This is the most efficient approach. We maintain an array (let's call it `sub`) that stores the smallest ending element of an increasing subsequence of a certain length.

* State:
    - `sub`: A sorted array where `sub[i]` is the smallest tail of all increasing subsequences of length `i+1`.

* Core Logic:
    - We iterate through each number `num` in the input `nums`.
    - For each `num`, we perform a binary search on our `sub` array.
    - If `num` is greater than all elements in `sub`, it means we can extend the longest subsequence found so far. We append `num` to `sub`, increasing the LIS length by 1.
    - If `num` is not greater than all elements, we find the smallest element in `sub` that is greater than or equal to `num` and replace it with `num`. This helps us potentially form a longer LIS later with a smaller tail. For example, if `sub` is `[2, 5, 7]` and `num` is `6`, we replace `7` with `6` to get `[2, 5, 6]`. This doesn't change the current LIS length, but an increasing subsequence of length 3 now ends with a smaller number (6 instead of 7), which makes it easier to extend later.

* Result:
    - The length of the `sub` array at the end gives the length of the LIS.

* Complexity:
    - Time: O(N log N) because for each of the N elements, we do a binary search which takes O(log N).
    - Space: O(N) for the `sub` array in the worst case.
"""

from typing import List
import bisect

class Solution:
    # Approach 1: Memoized Recursion
    def lengthOfLIS_memo(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [[-1]*(n+1) for _ in range(n)]

        def solve(i: int, prev_index: int) -> int:
            # Base case: reached the end of the array
            if i == n:
                return 0

            # Return memoized result if available
            if dp[i][prev_index+1] != -1 : return dp[i][prev_index+1]
            
            # Option 1: Don't take the current element
            ans = solve(i+1, prev_index)

            # Option 2: Take the current element if it's valid
            if prev_index == -1 or nums[i] > nums[prev_index]:
                ans = max(ans, 1 + solve(i+1, i))

            # Memoize and return the result
            dp[i][prev_index+1] = ans
            return ans

        return solve(0, -1)
    
    # Approach 2: Tabulation (O(n^2))
    # This uses a 2D DP table, mirroring the recursive solution.
    def lengthOfLIS_tabulation(self,nums:List[int]) -> int:
        n = len(nums)
        dp = [[0]*(n+1) for _ in range(n+1)]

        for i in range(n-1,-1,-1):
            for prev_index in range(i-1,-2,-1):
                take = 0
                if prev_index == -1 or nums[i] > nums[prev_index]:
                    take = 1 + dp[i+1][i+1] # new prev index is the curr index
                
                not_take = dp[i+1][prev_index+1]
                dp[i][prev_index+1] = max(take,not_take)

        return dp[0][0]
                
    # Approach 2: Tabulation (Bottom-Up DP) - Space Optimized (using 1D arrays for current and next states)
    def lengthOfLIS_tabulation_space_optimized_2D(self, nums: List[int]) -> int:
        n = len(nums)
        # next_dp stores results for i+1, curr_dp stores results for i
        next_dp = [0] * (n + 1) 

        for i in range(n-1,-1,-1):
            curr_dp = [0] * (n + 1)
            for prev_index in range(i-1,-2,-1):
                take = 0
                if prev_index == -1 or nums[i] > nums[prev_index]:
                    take = 1 + next_dp[i+1] # new prev index is the curr index (i)
                
                not_take = next_dp[prev_index+1] # prev_index+1 maps -1 to 0, 0 to 1, etc.
                curr_dp[prev_index+1] = max(take, not_take)

            next_dp = curr_dp # Move current row to next for the next iteration

        return next_dp[0] # Result for solve(0, -1) which is dp[0][-1+1] = dp[0][0]
    
    #* Approach 2: Tabulation (Bottom-Up DP) - Classic 1D array (O(N^2) time, O(N) space)
    def lengthOfLIS_tabulation_1D_classic(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        dp = [1]*n
        # `parent` array to reconstruct the LIS
        parent = list(range(n))

        for i in range(n):
            for prev_index in range(i):
                if nums[i]>nums[prev_index] and 1+dp[prev_index] > dp[i]:
                    dp[i] = 1 + dp[prev_index]
                    parent[i] = prev_index

        max_len = 0
        last_index = -1
        for i in range(n):
            if dp[i] > max_len:
                max_len = dp[i]
                last_index = i

        # Reconstruct and print the LIS
        if last_index != -1:
            lis = []
            while parent[last_index] != last_index:
                lis.append(nums[last_index])
                last_index = parent[last_index]
            lis.append(nums[last_index])
            lis.reverse()
            print(f"  (Found LIS: {' '.join(map(str, lis))})")

        return max_len

    # Approach 3: Optimized with Binary Search (O(n log n))
    def lengthOfLIS_optimized(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        
        seq = [nums[0]]
        for i in range(1,len(nums)):
            if nums[i] > seq[-1]:
                # The number is greater than the last number in the sequence
                seq.append(nums[i])
            else:
                #find the index of the number which is not gereater than the curr num ie lower_bound
                index = bisect.bisect_left(seq,nums[i])
                #insert the current num in is correct place
                seq[index] = nums[i]

        return len(seq)

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
        ([10, 9, 2, 5, 3, 7, 101, 18], 4),
        ([0, 1, 0, 3, 2, 3], 4),
        ([7, 7, 7, 7, 7, 7, 7], 1),
        ([], 0),
        ([1, 2, 3, 4, 5], 5),
    ]
    
    print("--- Testing Memoized Recursion ---")
    test_solution(sol.lengthOfLIS_memo, test_cases)
    print("\n--- Testing Tabulation (2D DP) ---")
    test_solution(sol.lengthOfLIS_tabulation, test_cases)
    print("\n--- Testing Tabulation (2D DP) - Space Optimized ---")
    test_solution(sol.lengthOfLIS_tabulation_space_optimized_2D, test_cases)
    print("\n--- Testing Tabulation (1D DP Classic) ---")
    test_solution(sol.lengthOfLIS_tabulation_1D_classic, test_cases)
    print("\n--- Testing Optimized DP with Binary Search ---")
    test_solution(sol.lengthOfLIS_optimized, test_cases)



"""
Dry Run Example (Solution 3: Optimized O(n log n) Approach):
---------------
Input: nums = [10, 9, 2, 5, 3, 7, 101, 18]

Initialize sub = []

1. num = 10: sub is empty. i = 0. Append 10.
   sub = [10]

2. num = 9: bisect_left(sub, 9) -> i = 0. Replace sub[0] with 9.
   sub = [9]

3. num = 2: bisect_left(sub, 2) -> i = 0. Replace sub[0] with 2.
   sub = [2]

4. num = 5: bisect_left(sub, 5) -> i = 1. Append 5.
   sub = [2, 5]

5. num = 3: bisect_left(sub, 3) -> i = 1. Replace sub[1] with 3.
   sub = [2, 3]

6. num = 7: bisect_left(sub, 7) -> i = 2. Append 7.
   sub = [2, 3, 7]

7. num = 101: bisect_left(sub, 101) -> i = 3. Append 101.
   sub = [2, 3, 7, 101]

8. num = 18: bisect_left(sub, 18) -> i = 3. Replace sub[3] with 18.
   sub = [2, 3, 7, 18]

End of loop. The final `sub` is [2, 3, 7, 18].
The length of `sub` is 4.

✅ Final Answer: 4

Dry Run Example (Solution 2: Classic 1D DP):
---------------
Input: nums = [0, 1, 0, 3, 2, 3]
n = 6
dp = [1, 1, 1, 1, 1, 1]

i = 0, num = 0: dp=[1, 1, 1, 1, 1, 1]

i = 1, num = 1:
  j = 0: nums[1]>nums[0] (1>0). dp[1] = max(1, 1+dp[0]) = 2.
  dp=[1, 2, 1, 1, 1, 1]

i = 2, num = 0:
  j = 0: nums[2] not > nums[0].
  j = 1: nums[2] not > nums[1].
  dp=[1, 2, 1, 1, 1, 1]

i = 3, num = 3:
  j = 0: nums[3]>nums[0] (3>0). dp[3] = max(1, 1+dp[0]) = 2.
  j = 1: nums[3]>nums[1] (3>1). dp[3] = max(2, 1+dp[1]) = 3.
  j = 2: nums[3]>nums[2] (3>0). dp[3] = max(3, 1+dp[2]) = 3.
  dp=[1, 2, 1, 3, 1, 1]

... and so on.
Final dp will be [1, 2, 1, 3, 3, 4]. The max value is 4.
"""
