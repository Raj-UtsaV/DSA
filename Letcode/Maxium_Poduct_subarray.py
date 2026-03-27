"""
Problem Description:
--------------------
Give an integer array `nums`, find the contiguous subarray 
(containing at least one number) which has the largest product and return the product.
link : https://leetcode.com/problems/maximum-product-subarray

Example:
--------
Input: [2,3,-2,4]
Output: 6

Input: [-2,0,-1]
Output: 0

"""

#!IDEA
"""
This file shows three approaches to solve the maximum product subarray problem:
1. Brute force: compute products for all subarrays (O(n^2)).
   - Iterate start index `i`, then end index `j`, keep running product.
   - Track global `max_prod` across all subarray products.
   - Works for correctness; too slow when n is large.

2. Better dynamic programming: track min/max products up to current index (O(n)).
   - Use `cur_max` (max product ending at current position) and `cur_min` (min product ending at current position).
   - `cur_min` needed because a negative value may become max after multiplying another negative.
   - For each `x`:
       * `tmp_max = max(x, x*cur_max, x*cur_min)`
       * `cur_min = min(x, x*cur_max, x*cur_min)`
       * `cur_max = tmp_max`
       * `max_prod = max(max_prod, cur_max)`
   - O(1) space, handles negative numbers and zeros robustly.

3. Best two-direction pass: left/right cumulative products (O(n)).
   - Keep two running products: `left` (prefix product) and `right` (suffix product).
   - If either hits zero, reset to 1, because contiguous subarray chain breaks at 0.
   - For each i: multiply `left` by nums[i], `right` by nums[n-1-i], update max.
   - Captures cases where maximum product subarray is between zero crossings.

Edge cases:
- Empty `nums` returns 0 (in better/best for safe behavior).
- Single element handles negative or zero.
"""

from typing import List

class Solution:
    def maxProduct_brute(self, nums: List[int]) -> int:
        n = len(nums)
        max_prod = -10**18

        for i in range(n):
            curr = 1
            for j in range(i, n):
                curr *= nums[j]
                max_prod = max(max_prod, curr)

        return max_prod

    def maxProduct_better(self, nums: List[int]) -> int:
        if not nums:
            return 0

        cur_min = nums[0]
        cur_max = nums[0]
        max_prod = nums[0]

        for i in range(1, len(nums)):
            x = nums[i]
            temp_max = max(x, x * cur_max, x * cur_min)
            cur_min = min(x, x * cur_max, x * cur_min)
            cur_max = temp_max
            max_prod = max(max_prod, cur_max)

        return max_prod

    def maxProduct_best(self, nums: List[int]) -> int:
        if not nums:
            return 0

        n = len(nums)
        left = 1
        right = 1
        max_prod = -10**18

        for i in range(n):
            left = 1 if left == 0 else left
            right = 1 if right == 0 else right

            left *= nums[i]
            right *= nums[n - i - 1]
            max_prod = max(max_prod, left, right)

        return max_prod


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


if __name__ == "__main__":
    sol = Solution()
    test_cases = [
        ([2, 3, -2, 4], 6),
        ([-2, 0, -1], 0),
        ([-2], -2),
        ([-2, -3, -1], 6),
    ]

    print('Brute:')
    test_solution(sol.maxProduct_brute, test_cases)
    print('\nBetter:')
    test_solution(sol.maxProduct_better, test_cases)
    print('\nBest:')
    test_solution(sol.maxProduct_best, test_cases)    
