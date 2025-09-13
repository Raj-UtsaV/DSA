"""
Given an array of distinct integers candidates and a target integer target,
return a list of all unique combinations of candidates where the chosen
numbers sum to target. You may return the combinations in any order.

The same number may be chosen from candidates an unlimited number of times.
Two combinations are unique if the frequency of at least one of the chosen
numbers is different.

Example 1:

Input: candidates = [2,3,6,7], target = 7
Output: [[2,2,3],[7]]

"""

#!IDEA
"""
Use recursion (backtracking).
At each index, choose:
- Take current candidate (can reuse same index)
- Skip current candidate (move to next index)
Stop when total == target (valid) or > target (invalid).
"""


from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        n = len(candidates)

        def backtrack(i: int, path: List[int], total: int):
            if total == target:
                res.append(path.copy())
                return
            if i >= n or total > target:
                return

            # Choice 1: take candidates[i]
            path.append(candidates[i])
            backtrack(i, path, total + candidates[i])  # stay at i (reuse allowed)
            path.pop()

            # Choice 2: skip candidates[i]
            backtrack(i + 1, path, total)

        backtrack(0, [], 0)
        return res


# --- Testing System ---
def test_solution(func, test_cases):
    for idx, (candidates, target, expected) in enumerate(test_cases, 1):
        output = func(candidates, target)
        # Sort inner lists and outer list for order-independent comparison
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
        ([2,3,6,7], 7, [[2,2,3],[7]]),
        ([2,3,5], 8, [[2,2,2,2],[2,3,3],[3,5]]),
        ([2], 1, []),
        ([1], 1, [[1]]),
    ]
    
    test_solution(sol.combinationSum, test_cases)
