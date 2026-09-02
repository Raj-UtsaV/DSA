"""Canonical solution metadata.

Problem Number: 36
Problem Title: Valid Sudoku
Platform: LeetCode
Difficulty: Medium
Official Platform Topics: Array, Hash Table, Matrix
Study Tags: Constraint validation
Canonical URL: https://leetcode.com/problems/valid-sudoku/
"""

"""
Problem Description:
--------------------
LeetCode 36. Valid Sudoku
Link: https://leetcode.com/problems/valid-sudoku/

Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:
1. Each row must contain the digits 1-9 without repetition.
2. Each column must contain the digits 1-9 without repetition.
3. Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.

Note:
- A Sudoku board (partially filled) could be valid but is not necessarily solvable.
- The board contains digits '1'-'9' and the character '.'.

Example:
--------
Input: board = 
[["5","3",".",".","7",".",".",".","."],
 ["6",".",".","1","9","5",".",".","."],
 [".","9","8",".",".",".",".","6","."],
 ["8",".",".",".","6",".",".",".","3"],
 ["4",".",".","8",".","3",".",".","1"],
 ["7",".",".",".","2",".",".",".","6"],
 [".","6",".",".",".",".","2","8","."],
 [".",".",".","4","1","9",".",".","5"],
 [".",".",".",".","8",".",".","7","9"]]
Output: true

"""

#!IDEA
"""
The most efficient way to check for a valid Sudoku board is to 
iterate through the board once and use data structures to keep track of the numbers seen in each row, column, and 3x3 sub-box.

- We can use three lists of sets (or dictionaries):
  1. `rows`: A list of 9 sets, where `rows[i]` stores the numbers seen in the i-th row.
  2. `cols`: A list of 9 sets, where `cols[j]` stores the numbers seen in the j-th column.
  3. `boxes`: A list of 9 sets, where `boxes[k]` stores the numbers seen in the k-th 3x3 box.

- The index for the box `k` can be calculated from the row `i` and column 
`j` as `k = (i // 3) * 3 + (j // 3)`.

- We iterate through each cell `(i, j)` of the board:
  - If the cell is not empty (i.e., not '.'), we get its number.
  - We check if this number is already in the set for the current row 
  (`rows[i]`), column (`cols[j]`), or box (`boxes[k]`).
  - If it is, we have found a duplicate, and the board is invalid. We return `False`.
  - If it's not a duplicate, we add the number to all three corresponding sets.

- If we finish iterating through the entire board without finding any 
duplicates, the board is valid, and we return `True`.
"""

from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        for i in range(9):
            for j in range(9):
                num = board[i][j]
                if num == ".":
                    continue

                # Check row
                if num in rows[i]:
                    return False
                rows[i].add(num)

                # Check column
                if num in cols[j]:
                    return False
                cols[j].add(num)

                # Check 3x3 box
                box_index = (i // 3) * 3 + (j // 3)
                if num in boxes[box_index]:
                    return False
                boxes[box_index].add(num)

        return True

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
        ([["5","3",".",".","7",".",".",".","."],
        ["6",".",".","1","9","5",".",".","."], [".","9","8",".",".",".",".","6","."],
        ["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],
        ["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],
        [".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]], True),

        ([["8","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],
        [".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],
        ["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],
        [".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],
        [".",".",".",".","8",".",".","7","9"]], False),
    ]

    test_solution(sol.isValidSudoku, test_cases)
