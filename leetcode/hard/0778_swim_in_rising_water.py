"""Canonical solution metadata.

Problem Number: 778
Problem Title: Swim in Rising Water
Platform: LeetCode
Difficulty: Hard
Official Platform Topics: Array, Binary Search, Depth-First Search, Breadth-First Search, Union-Find, Minimax, Heap (Priority Queue), Matrix, Dijkstra's Algorithm
Study Tags: Minimax path
Canonical URL: https://leetcode.com/problems/swim-in-rising-water/
"""

"""
Problem Description:
--------------------
LeetCode 778. Swim in Rising Water
Link: https://leetcode.com/problems/swim-in-rising-water/

You are given an n x n integer matrix grid where grid[i][j] represents the
elevation at that point (i, j).

The rain starts to fall. At time t, the depth of the water everywhere is t.
You can swim from a square to another 4-directionally adjacent square if
and only if the elevation of both squares individually is at most t. You can
swim infinite distances in zero time. Of course, you must stay within the
boundaries of the grid during your swim.

You start at the top-left square (0, 0). Return the least time until you can
reach the bottom-right square (n - 1, n - 1).

Example:
--------
Input: grid = [[0,1,2,3,4],[24,23,22,21,5],[12,13,14,15,16],
               [11,17,18,19,20],[10,9,8,7,6]]
Output: 16
Explanation: The final path is 0 -> 1 -> 2 -> 3 -> 4 -> 5 -> 16 -> 15 ->
14 -> 13 -> 12 -> 11 -> 10 -> 9 -> 8 -> 7 -> 6.
At time 16, every cell on this path has an elevation <= 16. This is the
minimum time required to connect the start and end points.

"""

#!IDEA
"""
This problem can be modeled as finding a path from the top-left to the
bottom-right corner of a grid that minimizes the maximum elevation along
the path. This is a classic shortest path problem on a graph, which can be
solved efficiently using a modification of Dijkstra's algorithm.

--- Solution: Dijkstra's Algorithm on a Grid ---

* State:
    - We use a min-heap (priority queue) to explore paths. Each element in
      the heap will be a tuple `(time, row, col)`.
    - `time`: The maximum elevation encountered so far on the path to `(row, col)`.
      This is equivalent to the minimum time `t` required to reach this cell.
    - `(row, col)`: The coordinates of the cell.
    - `visited`: A 2D boolean array to keep track of cells for which we have
      already found the minimum time, to avoid cycles and redundant work.

* Core Logic:
    1.  **Initialization**:
        - Create a min-heap and push the starting cell: `(grid[0][0], 0, 0)`.
          The initial time is the elevation of the start cell itself.
        - Initialize a `visited` grid of the same size, with all values set
          to `False`.

    2.  **Processing (Dijkstra's Loop)**:
        - While the heap is not empty, extract the cell with the smallest
          `time` from the heap. Let this be `(time, r, c)`.
        - If this cell `(r, c)` has already been visited, skip it.
        - Mark `(r, c)` as visited.
        - If `(r, c)` is the destination `(n-1, n-1)`, we have found the path
          with the minimum possible maximum elevation. The current `time` is
          our answer, so we can return it.

    3.  **Exploration**:
        - For the current cell `(r, c)`, explore its four adjacent neighbors
          `(nr, nc)`.
        - For each valid (within bounds) and unvisited neighbor:
            - The time required to reach this neighbor `(nr, nc)` via the
              current path is `max(time, grid[nr][nc])`. This is because we
              must wait until the water level is high enough to cover both
              the current path's requirement (`time`) and the neighbor's own
              elevation.
            - Push `(max(time, grid[nr][nc]), nr, nc)` onto the heap.

* Result:
    - The algorithm guarantees that the first time we extract the destination
      cell `(n-1, n-1)` from the heap, its associated `time` is the minimum
      possible. This is because Dijkstra's always explores the path with the
      lowest "cost" (in this case, lowest max elevation) first.

* Complexity:
    - Time complexity: O(N*N * log(N*N)), where N is the dimension of the
      grid. Each of the N*N cells is pushed and popped from the heap at most
      once. Heap operations take O(log(K)) where K is heap size (at most N*N).
    - Space complexity: O(N*N) for the `visited` grid and the heap.
"""

from typing import List
import heapq

class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0

        n = len(grid)
        visited = [[False]*n for _ in range(n)]

        # Heap stores (time, row, col)
        heap = [(grid[0][0], 0, 0)]
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        while heap:
            time, r, c = heapq.heappop(heap)

            if r == n - 1 and c == n - 1:
                return time

            if visited[r][c]:
                continue
            visited[r][c] = True

            for dr, dc in dirs:
                nr, nc = r + dr, c + dc

                if 0 <= nr < n and 0 <= nc < n and not visited[nr][nc]:
                    new_time = max(time, grid[nr][nc])
                    heapq.heappush(heap, (new_time, nr, nc))

        return -1


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
        ([[0, 2], [1, 3]], 3),
        (
            [
                [0, 1, 2, 3, 4],
                [24, 23, 22, 21, 5],
                [12, 13, 14, 15, 16],
                [11, 17, 18, 19, 20],
                [10, 9, 8, 7, 6]
            ],
            16
        ),
        ([[3, 2], [0, 1]], 3),
        ([[10, 12, 0, 1], [11, 14, 2, 3], [4, 5, 6, 7], [13, 9, 8, 15]], 12),
    ]

    test_solution(sol.swimInWater, test_cases)

"""
Dry Run Example:
---------------
Input: grid = [[0, 2], [1, 3]]
n = 2

1. Init:
   - visited = [[F, F], [F, F]]
   - heap = [(0, 0, 0)]  # (grid[0][0], 0, 0)

2. Loop 1:
   - Pop (0, 0, 0). time=0, r=0, c=0.
   - Not destination.
   - visited[0][0] = True.
   - Neighbors of (0,0): (0,1) and (1,0).
   - Neighbor (0,1):
     - new_time = max(time, grid[0][1]) = max(0, 2) = 2.
     - Push (2, 0, 1) to heap.
   - Neighbor (1,0):
     - new_time = max(time, grid[1][0]) = max(0, 1) = 1.
     - Push (1, 1, 0) to heap.
   - heap is now [(1, 1, 0), (2, 0, 1)].

3. Loop 2:
   - Pop (1, 1, 0). time=1, r=1, c=0.
   - Not destination.
   - visited[1][0] = True.
   - Neighbors of (1,0): (0,0) [visited] and (1,1).
   - Neighbor (1,1):
     - new_time = max(time, grid[1][1]) = max(1, 3) = 3.
     - Push (3, 1, 1) to heap.
   - heap is now [(2, 0, 1), (3, 1, 1)].

4. Loop 3:
   - Pop (2, 0, 1). time=2, r=0, c=1.
   - Not destination.
   - visited[0][1] = True.
   - Neighbors of (0,1): (0,0) [visited] and (1,1).
   - Neighbor (1,1):
     - new_time = max(time, grid[1][1]) = max(2, 3) = 3.
     - Push (3, 1, 1) to heap.
   - heap is now [(3, 1, 1), (3, 1, 1)].

5. Loop 4:
   - Pop (3, 1, 1). time=3, r=1, c=1.
   - This is the destination (n-1, n-1).
   - ✅ Return time = 3.
"""
