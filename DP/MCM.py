"""
Problem Description:
--------------------
[problem:] Matrix Chain Multiplication (MCM)
[link:] https://www.geeksforgeeks.org/matrix-chain-multiplication-dp-8/
[description:] Given a sequence of matrices, find the most efficient way to multiply
these matrices together. The problem is not to perform the multiplications, but to
decide the sequence of the matrix multiplications.

You are given an array `arr[]` of size `n` which represents a chain of `n-1`
matrices such that the `i-th` matrix `A_i` is of dimension `arr[i-1] x arr[i]`.

Find the minimum number of scalar multiplications needed to compute the product
of the matrices.

Example:
--------
Input: arr = [40, 20, 30, 10, 30]
Output: 26000
Explanation:
The input represents 4 matrices: A1(40x20), A2(20x30), A3(30x10), A4(10x30).
One possible parenthesization is (A1(A2A3))A4 which costs
(20*30*10) + (40*20*10) + (40*10*30) = 6000 + 8000 + 12000 = 26000.
This is the minimum cost.

"""

#!IDEA
"""
This is a classic dynamic programming problem. We want to find the minimum cost to multiply a chain of matrices. The key idea is that the final multiplication will be between two sub-chains. We need to find the optimal split point.

--- Solution 1: Memoized Recursion (Top-Down DP) ---

*   **State**:
    - `solve(i, j)`: Represents the minimum cost to multiply the chain of matrices
      from `A_i` to `A_j`. The dimensions of matrix `A_k` are `arr[k-1] x arr[k]`.
    - Our goal is to find `solve(1, n-1)`.

*   **Base Case**:
    - If `i == j`, we have only one matrix. No multiplication is needed.
      So, `solve(i, j) = 0`.

*   **Core Logic (Recursive Formulation)**:
    - To compute `solve(i, j)`, we decide where to place the last parenthesis.
      We can split the chain at any matrix `k` where `i <= k < j`.
    A split at `k` means we first compute `(A_i * ... * A_k)` and
    `(A_{k+1} * ... * A_j)`, and then multiply these two resulting matrices.
    - The cost for a split at `k` is:
      `solve(i, k) + solve(k+1, j) + (arr[i-1] * arr[k] * arr[j])`
      (cost of left part + cost of right part + cost of final multiplication)
    - We take the minimum cost over all possible split points `k`.

*   **Optimization (Memoization)**:
    - This recursive approach has overlapping subproblems. We use a 2D DP table
      `dp[i][j]` to store the results of `solve(i, j)` to avoid re-computation.

*   **Complexity**:
    - Time: O(N^3) due to three nested loops (i, j, and k).
    - Space: O(N^2) for the DP table + O(N) for recursion stack.

--- Solution 2: Tabulation (Bottom-Up DP) ---

*   **Core Logic**:
    - We convert the recursive solution to an iterative one.
    - We fill the `dp` table diagonally, considering chains of increasing length `L`.
    - For each length `L` from 2 to `n-1`, we iterate through all possible start
      indices `i`. The end index `j` is `i + L - 1`.
    - For each `(i, j)` pair, we iterate through all split points `k` from `i`
      to `j-1` to find the minimum cost, using previously computed values from the `dp` table.

*   **Complexity**:
    - Time: O(N^3)
    - Space: O(N^2)
"""

from typing import List

class Solution:
    # Approach 1: Memoized Recursion
    def matrixMultiplication_memo(self, arr: List[int]) -> int:
        n = len(arr)
        dp = [[-1] * n for _ in range(n)]

        def solve(i: int, j: int) -> int:
            if i == j:
                return 0

            if dp[i][j] != -1:
                return dp[i][j]

            mini = float("inf")
            for k in range(i, j):
                cost = (arr[i - 1] * arr[k] * arr[j]) + \
                       solve(i, k) + solve(k + 1, j)
                mini = min(mini, cost)

            dp[i][j] = mini
            return dp[i][j]

        return solve(1, n - 1)

    # Approach 2: Tabulation
    def matrixMultiplication_tab(self, arr: List[int]) -> int:
        n = len(arr)
        dp = [[0] * n for _ in range(n)]

        # L is the chain length
        for L in range(2, n):
            for i in range(1, n - L + 1):
                j = i + L - 1
                dp[i][j] = float('inf')
                for k in range(i, j):
                    cost = dp[i][k] + dp[k + 1][j] + \
                           arr[i - 1] * arr[k] * arr[j]
                    dp[i][j] = min(dp[i][j], cost)

        return dp[1][n - 1]

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
        ([10, 20, 30], 6000),
        ([10, 20, 30, 40, 30], 30000),
        ([40, 20, 30, 10, 30], 26000),
        ([2, 1, 3, 4], 20) # Corrected expected output from 13 to 20
    ]

    print("--- Testing Memoized Recursion ---")
    test_solution(sol.matrixMultiplication_memo, test_cases)
    print("\n--- Testing Tabulation ---")
    test_solution(sol.matrixMultiplication_tab, test_cases)