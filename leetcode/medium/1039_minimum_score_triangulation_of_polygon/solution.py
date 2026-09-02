"""Canonical solution metadata.

Problem Number: 1039
Problem Title: Minimum Score Triangulation of Polygon
Platform: LeetCode
Difficulty: Medium
Official Platform Topics: Array, Dynamic Programming, Triangulation, Polygons
Study Tags: Interval DP
Canonical URL: https://leetcode.com/problems/minimum-score-triangulation-of-polygon/
"""

"""
Problem Description:
--------------------
LeetCode 516. Minimum Score Triangulation of Polygon
Link: https://leetcode.com/problems/minimum-score-triangulation-of-polygon/

You have a convex n-sided polygon where each vertex has a value given in the array `values`.
You need to triangulate the polygon into `n-2` triangles. The score of a triangulation is the sum of the scores of its triangles.
The score of a triangle with vertices i, j, and k is `values[i] * values[j] * values[k]`.
Return the minimum possible score of a triangulation of the polygon.

Example:
--------
Input: values = [1,2,3]
Output: 6
Explanation: The polygon is a triangle, and its score is 1*2*3 = 6.

Input: values = [3,7,4,5]
Output: 144
Explanation: There are two possible triangulations.
The first triangulation has score 3*7*5 + 3*4*5 = 105 + 60 = 165.
The second triangulation has score 3*7*4 + 3*4*5 = 84 + 60 = 144.
The minimum score is 144.

"""

#!IDEA
"""
This problem can be solved using dynamic programming. We want to find the minimum score to triangulate a polygon.

Let's define `solve(i, j)` as the minimum score to triangulate the polygon formed by vertices from index `i` to `j` in the `values` array. Our goal is to find `solve(0, n-1)`.

1.  **Recursive Formulation**:
    Consider the polygon formed by vertices `i, i+1, ..., j`. The edge `(i, j)` must form a triangle with some other vertex `k` where `i < k < j`.
    When we form the triangle `(i, k, j)`, its score is `values[i] * values[k] * values[j]`.
    This triangle splits the original polygon `(i, ..., j)` into two smaller sub-polygons:
    - One formed by vertices `(i, ..., k)`.
    - Another formed by vertices `(k, ..., j)`.

    The total score for choosing vertex `k` is:
    `score(k) = (values[i] * values[k] * values[j]) + solve(i, k) + solve(k, j)`

    To find the minimum score for the polygon `(i, ..., j)`, we must try every possible intermediate vertex `k` and take the minimum:
    `solve(i, j) = min(score(k))` for all `k` from `i+1` to `j-1`.

2.  **Base Case**:
    If we have fewer than 3 vertices (i.e., `j <= i + 1`), we cannot form a triangle. So, the score is 0. This is our base case: `if i + 1 >= j: return 0`.

3.  **Memoization**:
    This recursive approach has overlapping subproblems. For example, `solve(2, 5)` might be needed by both `solve(0, 5)` and `solve(2, 7)`. To avoid re-computation, we use a 2D DP table (`dp[i][j]`) to store the results of `solve(i, j)`. Before computing, we check if the value is already in the table.

The final answer will be the result of `solve(0, n-1)`, where `n` is the number of vertices.
"""

from typing import List

class Solution:
    def minScoreTriangulation(self, values: List[int]) -> int:
        n = len(values)
        dp = [[-1] * n for _ in range(n)]

        def solve(i: int, j: int) -> int:
            # Base case: If there are less than 3 vertices, no triangle can be formed.
            if i + 1 >= j:
                return 0

            # If the result is already computed, return it.
            if dp[i][j] != -1:
                return dp[i][j]

            ans = float('inf')
            # Try all possible intermediate vertices 'k' to form triangle (i, k, j).
            for k in range(i + 1, j):
                cost = values[i] * values[k] * values[j] + solve(i, k) + solve(k, j)
                ans = min(ans, cost)

            # Memoize the result.
            dp[i][j] = ans
            return ans

        return solve(0, n - 1)

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
        ([1, 2, 3], 6),
        ([3, 7, 4, 5], 144),
        ([1, 3, 1, 4, 1, 5], 13),
    ]

    test_solution(sol.minScoreTriangulation, test_cases)

"""
Dry Run Example:
---------------
Input: values = [3, 7, 4, 5], n = 4

🎯 Goal: solve(0, 3)

└── solve(0, 3)
    ├── k=1: triangle(0,1,3) -> v[0]*v[1]*v[3] + solve(0,1) + solve(1,3)
    │   ├── solve(0,1) -> returns 0 (base case)
    │   └── solve(1,3)
    │       └── k=2: triangle(1,2,3) -> v[1]*v[2]*v[3] + solve(1,2) + solve(2,3)
    │           ├── solve(1,2) -> returns 0
    │           └── solve(2,3) -> returns 0
    │           Total for solve(1,3) = 7*4*5 + 0 + 0 = 140. dp[1][3] = 140.
    │       Total for k=1 = 3*7*5 + 0 + 140 = 105 + 140 = 245.
    │
    ├── k=2: triangle(0,2,3) -> v[0]*v[2]*v[3] + solve(0,2) + solve(2,3)
    │   ├── solve(0,2)
    │   │   └── k=1: triangle(0,1,2) -> v[0]*v[1]*v[2] + solve(0,1) + solve(1,2)
    │   │       ├── solve(0,1) -> returns 0
    │   │       └── solve(1,2) -> returns 0
    │   │       Total for solve(0,2) = 3*7*4 + 0 + 0 = 84. dp[0][2] = 84.
    │   └── solve(2,3) -> returns 0 (base case)
    │   Total for k=2 = 3*4*5 + 84 + 0 = 60 + 84 = 144.
    │
    └── ans = min(245, 144) = 144.

✅ Final Answer: 144
"""
