"""Canonical solution metadata.

Problem Number: 40
Problem Title: Combination Sum II
Platform: LeetCode
Difficulty: Medium
Official Platform Topics: Array, Backtracking
Study Tags: Duplicate pruning
Canonical URL: https://leetcode.com/problems/combination-sum-ii/
"""

"""
LeetCode 40. Combination Sum II
Link: https://leetcode.com/problems/combination-sum-ii/

Given a collection of candidate numbers (candidates) and a target number (target),
find all unique combinations in candidates where the candidate numbers sum to target.
Each number in candidates may only be used once in the combination.

Note: The solution set must not contain duplicate combinations.

Example 1:
Input: candidates = [10,1,2,7,6,1,5], target = 8
Output: [[1,1,6],[1,2,5],[1,7],[2,6]]
"""

#!IDEA
"""
Use backtracking.
- Sort candidates to group duplicates.
- At each index, we can choose to include candidates[i] or skip it.
- To avoid duplicates: when looping, if candidates[i] == candidates[i-1] and i > start,
  skip it (ensures duplicates are only used once at each depth).
- Each candidate can be used at most once, so we always recurse with i+1.
- Stop if total == target (valid) or > target (invalid).
"""


from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        n = len(candidates)

        def backtrack(start: int, path: List[int], total: int):
            if total == target:
                res.append(path[:])
                return
            if total>target  or start>=n:
                return

            for i in range(start,n):
                if i>start and candidates[i] == candidates[i-1]:
                    continue

                path.append(candidates[i])
                backtrack(i+1,path,total+candidates[i])
                path.pop()


        backtrack(0, [], 0)
        return res


# --- Testing System ---
def test_solution(func, test_cases):
    for idx, (candidates, target, expected) in enumerate(test_cases, 1):
        output = func(candidates, target)
        sorted_output = sorted([sorted(comb) for comb in output])
        sorted_expected = sorted([sorted(comb) for comb in expected])
        if sorted_output == sorted_expected:
            print(f"Test case {idx}: ✅ Passed")
        else:
            print(f"Test case {idx}: ❌ Failed")
            print(f"  Input: candidates={candidates}, target={target}")
            print(f"  Output: {output}")
            print(f"  Expected: {expected}")


# --- Example Test Cases ---
if __name__ == "__main__":
    sol = Solution()
    test_cases = [
        ([10,1,2,7,6,1,5], 8, [[1,1,6],[1,2,5],[1,7],[2,6]]),
        ([2,5,2,1,2], 5, [[1,2,2],[5]]),
        ([3,1,3,5,1,1], 8, [[1,1,1,5],[1,1,3,3],[3,5]]),
    ]

    test_solution(sol.combinationSum2, test_cases)
