"""Canonical solution metadata.

Problem Number: 417
Problem Title: Pacific Atlantic Water Flow
Platform: LeetCode
Difficulty: Medium
Official Platform Topics: Array, Depth-First Search, Breadth-First Search, Matrix
Study Tags: Reverse reachability
Canonical URL: https://leetcode.com/problems/pacific-atlantic-water-flow/
"""

"""
Problem Description:
--------------------
[problem:] LeetCode 417. Pacific Atlantic Water Flow
[link:] https://leetcode.com/problems/pacific-atlantic-water-flow/
[description:] You are given an m x n integer matrix heights representing the height of each 
unit cell in a continent. The Pacific ocean touches the continent's top and left edges, and the 
Atlantic ocean touches the continent's bottom and right edges.

Water can flow from one cell to another adjacent cell (up, down, left, or right) if the adjacent 
cell's height is less than or equal to the current cell's height. Water flows from any cell adjacent 
to an ocean into the ocean.

Return a 2D list of grid coordinates result where result[i] = [ri, ci] denotes that rain water can 
low from cell (ri, ci) to both the Pacific and Atlantic oceans.

Example:
--------
Input: heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
Output: [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]

"""

#!IDEA
"""
The problem asks for all cells that can flow to both the Pacific and Atlantic oceans. 
A brute-force approach of starting a traversal from every cell to see if it reaches 
both oceans would be inefficient (O((N*M)^2)).

A more optimal approach is to reverse the problem: find all cells that can be reached *from* the Pacific Ocean 
and all cells that can be reached *from* the Atlantic Ocean. The intersection of these two sets will be our answer.

--- Solution: Multi-source BFS from Oceans ---

* State:
    - `pac_reachable`: A boolean matrix of the same size as `heights`. `pac_reachable[i][j]` 
        is true if cell (i, j) can flow to the Pacific.
    - `atl_reachable`: A boolean matrix of the same size as `heights`. `atl_reachable[i][j]` 
        is true if cell (i, j) can flow to the Atlantic.
    - Two queues, one for the Pacific BFS and one for the Atlantic BFS.

* Core Logic:
    1.  **Initialization**:
        - Create two queues, `pac_queue` and `atl_queue`.
        - Populate `pac_queue` with all cells adjacent to the Pacific (top row and left column). 
            Mark these cells as reachable in `pac_reachable`.
        - Populate `atl_queue` with all cells adjacent to the Atlantic (bottom row and right column). 
            Mark these cells as reachable in `atl_reachable`.

    2.  **BFS Traversal**:
        - Define a BFS helper function that takes a queue and a `reachable` matrix.
        - The BFS will explore "inwards" from the ocean. When at a cell `(x, y)`, we explore its neighbors `(nx, ny)`.
        - A neighbor `(nx, ny)` can be reached from `(x, y)` if `heights[nx][ny] >= heights[x][y]`. 
            This is the reverse of the water flow condition, representing that water can flow from the higher `(nx, ny)` 
            down to `(x, y)` and then to the ocean.
        - If a valid, unvisited neighbor is found, mark it as reachable and add it to the queue.

    3.  **Run BFS**:
        - Run the BFS once for the Pacific starting with `pac_queue` and updating `pac_reachable`.
        - Run the BFS again for the Atlantic starting with `atl_queue` and updating `atl_reachable`.

* Result:
    - Iterate through the entire grid. If a cell `(i, j)` is marked as true in both `pac_reachable` and
      `atl_reachable`, add its coordinates to the final result list.

* Complexity:
    - Time complexity: O(N * M), where N and M are the dimensions of the matrix. Each cell is visited 
    at most twice (once for each BFS).
    - Space complexity: O(N * M) for the queues and the visited matrices.
"""

from typing import List
from collections import deque

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights or not heights[0]:
            return []

        n, m = len(heights), len(heights[0])
        pac_reachable = [[False] * m for _ in range(n)]
        atl_reachable = [[False] * m for _ in range(n)]

        pac_queue = deque()
        atl_queue = deque()

        # Initialize queues with border cells
        # Pacific borders (top and left)
        for j in range(m):
            if not pac_reachable[0][j]:
                pac_reachable[0][j] = True
                pac_queue.append((0, j))
        for i in range(n):
            if not pac_reachable[i][0]:
                pac_reachable[i][0] = True
                pac_queue.append((i, 0))

        # Atlantic borders (bottom and right)
        for j in range(m):
            if not atl_reachable[n - 1][j]:
                atl_reachable[n - 1][j] = True
                atl_queue.append((n - 1, j))
        for i in range(n):
            if not atl_reachable[i][m - 1]:
                atl_reachable[i][m - 1] = True
                atl_queue.append((i, m - 1))

        def bfs(queue: deque, reachable: List[List[bool]]):
            dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]
            while queue:
                x, y = queue.popleft()

                for dx, dy in dirs:
                    nx, ny = x + dx, y + dy

                    if 0 <= nx < n and 0 <= ny < m and not reachable[nx][ny]:
                        # We can flow "inland" if the new cell is higher or equal
                        if heights[nx][ny] >= heights[x][y]:
                            reachable[nx][ny] = True
                            queue.append((nx, ny))

        # Run BFS from both oceans
        bfs(pac_queue, pac_reachable)
        bfs(atl_queue, atl_reachable)

        ans = []
        for i in range(n):
            for j in range(m):
                if pac_reachable[i][j] and atl_reachable[i][j]:
                    ans.append([i, j])

        return ans

# --- Testing System ---
def test_solution(func, test_cases):
    for idx, (input_val, expected) in enumerate(test_cases, 1):
        output = func(input_val)
        # Sort both lists to compare regardless of order
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
        ([[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]], [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]),
        ([[1]], [[0,0]]),
        ([[2,1],[1,2]], [[0,0],[0,1],[1,0],[1,1]])
    ]

    test_solution(sol.pacificAtlantic, test_cases)




