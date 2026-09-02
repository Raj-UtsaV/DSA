"""Canonical solution metadata.

Problem Number: 51
Problem Title: N-Queens
Platform: LeetCode
Difficulty: Hard
Official Platform Topics: Array, Backtracking, Algorithm X
Study Tags: Constraint pruning
Canonical URL: https://leetcode.com/problems/n-queens/
"""

"""
LeetCode 51. N-Queens
Link: https://leetcode.com/problems/n-queens/

The n-queens puzzle is the problem of placing n queens on an n×n chessboard 
such that no two queens attack each other.

Example 1:
Input: n = 4
Output: 
[
 [".Q..",
  "...Q",
  "Q...",
  "..Q."],

 ["..Q.",
  "Q...",
  "...Q",
  ".Q.."]
]

Example 2:
Input: n = 1
Output: [["Q"]]
"""

#!IDEA
"""
We use backtracking:
- Place queens column by column (or row by row).
- For each column, try placing a queen in every row.
- Check if it's safe using either:
  (a) is_safe scanning (check left row, upper diagonal, lower diagonal).
  (b) Optimized sets (track columns, diag1=r-c, diag2=r+c).
- If placement is valid, place queen and recurse for next column.
- If col == n, store the solution.
- Backtrack: remove queen and try next row.

Time Complexity: O(N!) worst case
Space Complexity: O(N^2) for storing boards
"""

from typing import List

class Solution:
    # --- Method 1: Basic Backtracking with is_safe scanning ---
    def solveNQueens_basic(self, n: int) -> List[List[str]]:
        res = []
        board = [["."] * n for _ in range(n)]

        def is_safe(row, col):
            dup_row, dup_col = row, col

            #? upper diagonal (↖)
            while row >= 0 and col >= 0:
                if board[row][col] == "Q":
                    return False
                row -= 1
                col -= 1

            #? same row to the left (←)
            col = dup_col
            while col >= 0:
                if board[dup_row][col] == "Q":
                    return False
                col -= 1

            #? lower diagonal (↙)
            row, col = dup_row, dup_col
            while row < n and col >= 0:
                if board[row][col] == "Q":
                    return False
                row += 1
                col -= 1

            return True

        def backtrack(col):
            if col == n:
                res.append(["".join(r) for r in board])
                return

            for row in range(n):
                if is_safe(row, col):
                    board[row][col] = "Q"
                    backtrack(col + 1)
                    board[row][col] = "."

        backtrack(0)
        return res

    # --- Method 2: Optimized Backtracking with sets ---
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        board = [["."] * n for _ in range(n)]
        cols, diag1, diag2 = set(), set(), set()  # col, r-c, r+c

        def backtrack(r: int):
            if r == n:
                res.append(["".join(row) for row in board])
                return

            for c in range(n):
                if c in cols or (r - c) in diag1 or (r + c) in diag2:
                    continue

                # place queen
                board[r][c] = "Q"
                cols.add(c)
                diag1.add(r - c)
                diag2.add(r + c)

                backtrack(r + 1)

                # remove queen (backtrack)
                board[r][c] = "."
                cols.remove(c)
                diag1.remove(r - c)
                diag2.remove(r + c)

        backtrack(0)
        return res


# --- Testing System ---
def test_solution(func, test_cases):
    for idx, (n, expected_len) in enumerate(test_cases, 1):
        output = func(n)
        if len(output) == expected_len:
            print(f"Test case {idx}: ✅ Passed")
        else:
            print(f"Test case {idx}: ❌ Failed")
            print(f"  Input: n={n}")
            print(f"  Output length: {len(output)}")
            print(f"  Expected length: {expected_len}")


# --- Example Test Cases ---
if __name__ == "__main__":
    sol = Solution()
    test_cases = [
        (1, 1),   # [["Q"]]
        (4, 2),   # 2 solutions
        (5, 10),  # 10 solutions
    ]
    print("Testing Basic Method:")
    test_solution(sol.solveNQueens_basic, test_cases)
    print("\nTesting Optimized Method:")
    test_solution(sol.solveNQueens, test_cases)
