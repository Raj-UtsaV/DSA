"""Canonical solution metadata.

Problem Number: 90
Problem Title: Subsets II
Platform: LeetCode
Difficulty: Medium
Official Platform Topics: Array, Backtracking, Bit Manipulation
Study Tags: Duplicate pruning
Canonical URL: https://leetcode.com/problems/subsets-ii/
"""

"""
LeetCode 90. Subsets II
Link: https://leetcode.com/problems/subsets-ii/

Given an integer array nums that may contain duplicates, return all possible subsets 
(the power set). The solution set must not contain duplicate subsets. Return the solution in any order.

Example 1:
Input: nums = [1,2,2]
Output: [[],[1],[2],[1,2],[2,2],[1,2,2]]
"""

#!IDEA
"""
Use backtracking with duplicate skipping.
- Sort nums so duplicates are adjacent.
- At each recursion, append the current path to results (captures all subset sizes).
- Loop i from start..n-1:
    - If i > start and nums[i] == nums[i-1], skip (avoids duplicate subsets at same depth).
    - Choose nums[i], recurse with i+1, then backtrack.
This generates each unique subset exactly once.
"""


from typing import List


class Solution:
    def subsetsWithDup1(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        n = len(nums)

        def backtrack(i: int, path: List[int], prev_chosen: bool):
            if i == n:
                res.append(path.copy())
                return

            # Option 1: Exclude nums[i]
            backtrack(i + 1, path, False)

            # Option 2: Include nums[i]
            # BUT: if current == previous and previous was *not chosen*, skip to avoid duplicates
            if i > 0 and nums[i] == nums[i - 1] and not prev_chosen:
                return

            path.append(nums[i])
            backtrack(i + 1, path, True)
            path.pop()

        backtrack(0, [], False)
        return res

    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res: List[List[int]] = []
        n = len(nums)

        def backtrack(start: int, path: List[int]):
            res.append(path.copy())


            for i in range(start, n):
                if i > start and nums[i] == nums[i - 1]:
                    continue
                path.append(nums[i])
                backtrack(i + 1, path)
                path.pop()

        backtrack(0, [])
        return res


# --- Testing System ---
def test_solution(func, test_cases):
    for idx, (nums, expected) in enumerate(test_cases, 1):
        output = func(nums)
        # order-independent compare: sort inner lists and outer list
        sorted_output = sorted([sorted(sub) for sub in output])
        sorted_expected = sorted([sorted(sub) for sub in expected])
        if sorted_output == sorted_expected:
            print(f"Test case {idx}: ✅ Passed")
        else:
            print(f"Test case {idx}: ❌ Failed")
            print(f"  Input: nums={nums}")
            print(f"  Output: {output}")
            print(f"  Expected: {expected}")


# --- Example Test Cases ---
if __name__ == "__main__":
    sol = Solution()
    test_cases = [
        ([1,2,2], [[],[1],[2],[1,2],[2,2],[1,2,2]]),
        ([0], [[],[0]]),
        ([1,2,2,3], [[],
                      [1],[2],[3],
                      [1,2],[1,3],[2,2],[2,3],
                      [1,2,2],[1,2,3],[2,2,3],[1,2,2,3]]),
    ]
    test_solution(sol.subsetsWithDup, test_cases)
