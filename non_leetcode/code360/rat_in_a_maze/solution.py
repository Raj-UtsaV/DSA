"""Canonical solution metadata.

Problem Number: Not applicable
Problem Title: Rat in a Maze
Platform: Code360
Difficulty: Not reliably specified
Official Platform Topics: Not specified
Study Tags: Grid Backtracking, Path Enumeration
Canonical URL: https://www.naukri.com/code360/problems/rat-in-a-maze-_8842357
"""

"""
Rat in a Maze Problem
Link: https://www.naukri.com/code360/problems/rat-in-a-maze-_8842357

You are given an n x n matrix (maze) where:
- 1 means the cell is open,
- 0 means blocked.

The rat starts at (0,0) and needs to reach (n-1,n-1).
Allowed moves: Down ("D"), Right ("R").

Return all possible paths as strings.
"""

#!IDEA
"""
Use backtracking:
- Start from (0,0) and explore all valid moves (Down, Right).
- Keep track of current path in `ans`.
- If we reach bottom-right cell, store path in result.
- Backtrack by popping last move after recursion.
- The push/pop always occurs inside the `if` condition to avoid corrupting the path list.
"""

from typing import List

class Solution:
    def ratMaze(self, matrix: List[List[int]]) -> List[str]:
        n = len(matrix)
        res = []
        ans = []

        def backtrack(i, j):
            if i == n - 1 and j == n - 1:
                res.append("".join(ans))
                return

            # Directions: Down, Right
            directions = [(1, 0, "D"), (0, 1, "R")]  
            for r, c, move in directions:
                nr, nc = i + r, j + c
                if 0 <= nr < n and 0 <= nc < n and matrix[nr][nc] == 1:
                    ans.append(move)
                    backtrack(nr, nc)
                    ans.pop()

        if matrix[0][0] == 0 or matrix[n-1][n-1] == 0:
            return [-1]

        backtrack(0, 0)

        if not res:
            return [-1]

        return res


# --- Testing System ---
def test_solution(func, test_cases):
    for idx, (input_val, expected) in enumerate(test_cases, 1):
        output = func(input_val)
        if sorted(output) == sorted(expected):
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
        (
            [
                [1, 0, 0, 0],
                [1, 1, 0, 1],
                [0, 1, 0, 0],
                [1, 1, 1, 1]
            ],
            ['DRDDRR']
        ),
        (
            [
                [1, 0, 0, 0],
                [1, 0, 0, 1],
                [0, 1, 0, 0],
                [1, 1, 1, 1]
            ],
            [-1]
        ),
        (
            [
                [0, 0],
                [1, 1]
            ],
            [-1]
        ),
        (
            [
                [1, 1, 1],
                [1, 1, 1],
                [1, 1, 1]
            ],
            ['DDRR', 'DRDR', 'DRRD', 'RDDR', 'RDRD', 'RRDD']
        )
    ]
    test_solution(sol.ratMaze, test_cases)


"""
Dry Run Example:
---------------
Input: matrix = [[1, 0, 0, 0], [1, 1, 0, 1], [0, 1, 0, 0], [1, 1, 1, 1]]

1. backtrack(0, 0), path=[]
   - Move Down: path=["D"], call backtrack(1, 0)

2. backtrack(1, 0), path=["D"]
   - Move Down: blocked (matrix[2][0] == 0)
   - Move Right: path=["D", "R"], call backtrack(1, 1)

3. backtrack(1, 1), path=["D", "R"]
   - Move Down: path=["D", "R", "D"], call backtrack(2, 1)

4. backtrack(2, 1), path=["D", "R", "D"]
   - Move Down: path=["D", "R", "D", "D"], call backtrack(3, 1)

5. backtrack(3, 1), path=["D", "R", "D", "D"]
   - Move Down: out of bounds
   - Move Right: path=["D", "R", "D", "D", "R"], call backtrack(3, 2)

6. backtrack(3, 2), path=["D", "R", "D", "D", "R"]
   - Move Down: out of bounds
   - Move Right: path=["D", "R", "D", "D", "R", "R"], call backtrack(3, 3)

7. backtrack(3, 3), path=["D", "R", "D", "D", "R", "R"]
   - Base case i=n-1, j=n-1.
   - res.append("DRDDRR")
   - Return.

8. Backtracking continues, but no other paths are found.

Final Answer:
-------------
['DRDDRR']
"""
