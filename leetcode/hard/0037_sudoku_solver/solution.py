"""Canonical solution metadata.

Problem Number: 37
Problem Title: Sudoku Solver
Platform: LeetCode
Difficulty: Hard
Official Platform Topics: Array, Hash Table, Backtracking, Matrix, Algorithm X, Dancing Links
Study Tags: Constraint propagation
Canonical URL: https://leetcode.com/problems/sudoku-solver/
"""

"""
Problem Description:
--------------------
[problem:] LeetCode 37. Sudoku Solver
[link:] https://leetcode.com/problems/sudoku-solver/
[Brief description of the problem, input/output requirements, constraints, and examples]
Write a program to solve a Sudoku puzzle by filling the empty cells.
A sudoku solution must satisfy all of the following rules:
1. Each of the digits 1-9 must occur exactly once in each row.
2. Each of the digits 1-9 must occur exactly once in each column.
3. Each of the digits 1-9 must occur exactly once in each of the 9 3x3 sub-boxes of the grid.
The '.' character indicates empty cells. The function should modify the board in-place.

Example:
--------
Input: board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."], ... ]
Output: (board is modified in-place to the solved state)

"""

#!IDEA
"""
[Describe the approach/algorithm/logic used to solve the problem]
- We use backtracking to solve the Sudoku puzzle.
- The main idea is to try placing numbers from '1' to '9' in each empty cell.
- We define a recursive function, `backtrack()`, that attempts to fill the board.
- The function iterates through each cell (row by row, column by column).
- When it finds an empty cell ('.'), it tries to place each digit from '1' to '9'.
- For each digit, it checks if placing it in the current cell is valid (i.e., it doesn't violate Sudoku rules for the row, column, and 3x3 sub-grid).
- If the placement is valid, it places the digit and makes a recursive call to `backtrack()` to continue solving the rest of the board.
- If the recursive call returns `True`, it means a solution was found, so we propagate `True` up the call stack.
- If the recursive call returns `False`, it means the current placement led to a dead end. We must backtrack by resetting the cell to '.' and trying the next digit.
- If all digits from '1' to '9' have been tried for an empty cell and none lead to a solution, the function returns `False`.
- The base case for the recursion is when the entire board is scanned and no empty cells are found, which means the puzzle is solved, and we return `True`.
"""

from typing import List

class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        def is_possible(row, col, c):
            for i in range(9):
                # check column
                if board[i][col] == c:
                    return False
                # check row
                if board[row][i] == c:
                    return False
                # check 3x3 subgrid
                if board[3 * (row // 3) + i // 3][3 * (col // 3) + i % 3] == c:
                    return False
            return True

        def backtrack():
            for i in range(9):
                for j in range(9):
                    if board[i][j] == '.':
                        for num_char in "123456789":
                            if is_possible(i, j, num_char):
                                board[i][j] = num_char
                                if backtrack():
                                    return True
                                board[i][j] = '.'  # Backtrack
                        return False  # Trigger backtracking
            return True  # Solution found

        backtrack()


# --- Testing System ---
def test_solution(func, test_cases):
    def print_board(b, title):
        print(title)
        for row in b:
            print(f"  {row}")

    for idx, (board, expected) in enumerate(test_cases, 1):
        # Create a deep copy to avoid modifying the original test case board
        board_copy = [row[:] for row in board]
        func(board_copy)

        if board_copy == expected:
            print(f"Test case {idx}: ✅ Passed")
        else:
            print(f"Test case {idx}: ❌ Failed")
            print_board(board, "  Input Board:")
            print_board(board_copy, "  Output Board:")
            print_board(expected, "  Expected Board:")


# --- Example Test Cases ---
if __name__ == "__main__":
    sol = Solution()
    test_cases = [
        (
            [
                ["5","3",".",".","7",".",".",".","."],
                ["6",".",".","1","9","5",".",".","."],
                [".","9","8",".",".",".",".","6","."],
                ["8",".",".",".","6",".",".",".","3"],
                ["4",".",".","8",".","3",".",".","1"],
                ["7",".",".",".","2",".",".",".","6"],
                [".","6",".",".",".",".","2","8","."],
                [".",".",".","4","1","9",".",".","5"],
                [".",".",".",".","8",".",".","7","9"]
            ],
            [
                ["5","3","4","6","7","8","9","1","2"],
                ["6","7","2","1","9","5","3","4","8"],
                ["1","9","8","3","4","2","5","6","7"],
                ["8","5","9","7","6","1","4","2","3"],
                ["4","2","6","8","5","3","7","9","1"],
                ["7","1","3","9","2","4","8","5","6"],
                ["9","6","1","5","3","7","2","8","4"],
                ["2","8","7","4","1","9","6","3","5"],
                ["3","4","5","2","8","6","1","7","9"]
            ]
        )
    ]

    test_solution(sol.solveSudoku, test_cases)


"""
Dry Run Example:
---------------
board = [["5","3",".", ...], ...]

1. backtrack():
   - Scans until it finds board[0][2] == '.'
   - Loop num from '1' to '9':
     - Try num = '1': is_possible(0, 2, '1') -> True.
       - board[0][2] = '1'.
       - Call backtrack().
         - Scans until it finds board[0][3] == '.'
         - Loop num for (0,3):
           - Try num = '1': is_possible(0, 3, '1') -> False (row conflict).
           - Try num = '2': is_possible(0, 3, '2') -> True.
             - board[0][3] = '2'.
             - Call backtrack().
               - ... continues recursively.

   - If a recursive call eventually returns False (e.g., placing '2' at (0,3) leads to a dead end):
     - The call for (0,3) backtracks: board[0][3] = '.'
     - It continues its loop, trying '3', '4', etc. for (0,3).
     - If all numbers for (0,3) fail, it returns False.
     - The call for (0,2) receives False. It backtracks: board[0][2] = '.'
     - It continues its loop, trying '2', '3', etc. for (0,2).

This process continues until a full valid board is found or all possibilities are exhausted.
"""
