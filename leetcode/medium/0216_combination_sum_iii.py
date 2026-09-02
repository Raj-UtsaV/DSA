"""Canonical solution metadata.

Problem Number: 216
Problem Title: Combination Sum III
Platform: LeetCode
Difficulty: Medium
Official Platform Topics: Array, Backtracking
Study Tags: Fixed-depth search
Canonical URL: https://leetcode.com/problems/combination-sum-iii/
"""

"""
LeetCode 216. Combination Sum III
Link: https://leetcode.com/problems/combination-sum-iii/

Find all possible combinations of k numbers that add up to a number n, 
given that only numbers 1 to 9 
can be used and each combination should be a unique set of numbers.

Example 1:
Input: k = 3, n = 7
Output: [[1,2,4]]

Example 2:
Input: k = 3, n = 9
Output: [[1,2,6],[1,3,5],[2,3,4]]
"""

#!IDEA
"""
Use backtracking (binary choice: include/exclude each number 1..9).
- Keep track of current path, current total, and current index.
- Stop if path length > k or index >= 9.
- If total == n and path length == k, save path to result.
- At each index i, branch:
    1. Exclude nums[i]
    2. Include nums[i] (add to total), recurse, then backtrack
"""

from typing import List

class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        nums = list(range(1,10))
        res = []

        def backtrack(i: int, path: List[int], total: int):
            if len(path) > k or total > n:
                return
            if len(path) == k and total == n:
                res.append(path.copy())
                return
            if i >= 9:
                return

            # Exclude nums[i]
            backtrack(i+1, path, total)
            # Include nums[i]
            path.append(nums[i])
            backtrack(i+1, path, total + nums[i])
            path.pop()

        backtrack(0, [], 0)
        return res


# --- Testing System ---
def test_solution(func, test_cases):
    for idx, (k, n, expected) in enumerate(test_cases, 1):
        output = func(k, n)
        sorted_output = sorted([sorted(comb) for comb in output])
        sorted_expected = sorted([sorted(comb) for comb in expected])
        if sorted_output == sorted_expected:
            print(f"Test case {idx}: ✅ Passed")
        else:
            print(f"Test case {idx}: ❌ Failed")
            print(f"  Input: k={k}, n={n}")
            print(f"  Output: {output}")
            print(f"  Expected: {expected}")


# --- Example Test Cases ---
if __name__ == "__main__":
    sol = Solution()
    test_cases = [
        (3, 7, [[1,2,4]]),
        (3, 9, [[1,2,6],[1,3,5],[2,3,4]]),
        (4, 1, []), 
        (3, 15, [[1,5,9],[1,6,8],[2,4,9],[2,5,8],[2,6,7],[3,4,8],[3,5,7],[4,5,6]]),
        (9,45,[[1,2,3,4,5,6,7,8,9]]),
    ]
    test_solution(sol.combinationSum3, test_cases)
