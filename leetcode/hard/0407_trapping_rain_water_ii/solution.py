"""Canonical solution metadata.

Problem Number: 407
Problem Title: Trapping Rain Water II
Platform: LeetCode
Difficulty: Hard
Official Platform Topics: Array, Breadth-First Search, Heap (Priority Queue), Matrix
Study Tags: Boundary expansion
Canonical URL: https://leetcode.com/problems/trapping-rain-water-ii/
"""

"""
Problem Description:
--------------------
LeetCode 407. Trapping Rain Water II
Link: https://leetcode.com/problems/trapping-rain-water-ii/

Given an m x n integer matrix heightMap representing the height of each unit cell in a 2D elevation map, compute the volume of water it can trap after raining.

Example:
--------
Input: heightMap = [[1,4,3,1,3,2],[3,2,1,3,2,4],[2,3,3,2,3,1]]
Output: 4
Explanation: After the rain, water is trapped between the cells. The total volume of water trapped is 4.

"""

#!IDEA
"""
This problem can be solved using a priority queue (min-heap) and a variation of Breadth-First Search (BFS), similar to Dijkstra's algorithm. The core idea is to treat the border cells of the matrix as the initial "walls" of a container and explore inwards from the lowest point on the boundary.

1.  **Initialization**:
    - Create a `visited` matrix to keep track of cells we've processed.
    - Create a min-heap to store boundary cells. The heap will store tuples of `(height, row, col)`.
    - Add all cells on the border of the `heightMap` to the min-heap and mark them as visited. These cells form the initial container wall.

2.  **Processing**:
    - Initialize `water` trapped to 0.
    - While the min-heap is not empty, extract the cell with the minimum height `(h, x, y)`. This height `h` acts as the current water level, determined by the lowest point on the boundary of our explored area.

3.  **Exploration**:
    - For the extracted cell `(h, x, y)`, explore its four neighbors `(nx, ny)`.
    - If a neighbor is within bounds and has not been visited:
        - Mark the neighbor as visited.
        - Let the neighbor's height be `nh = heightMap[nx][ny]`.
        - The amount of water that can be trapped above this neighbor is determined by the current water level `h`.
        - If `nh < h`, it means water can be trapped. The amount is `h - nh`. Add this to the total `water`.
        - We then push this neighbor onto the heap. The height used for the heap entry is `max(h, nh)`. This is crucial: the new boundary height is the maximum of the current water level and the neighbor's own height. If we just pushed `(h, nx, ny)`, we are effectively "filling" the neighbor cell up to level `h` and treating it as part of the wall at that height.

4.  **Return Result**:
    - After the heap is empty, `water` will hold the total volume of trapped water.

This approach works because we are always processing the lowest possible "leak" point in our container wall. By expanding from there, we correctly calculate how much water can be held back by that boundary.
"""

from typing import List
import heapq

class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        if not heightMap or not heightMap[0]:
            return 0

        n, m = len(heightMap), len(heightMap[0])
        visited = [[False] * m for _ in range(n)]

        heap = []
        # Add all border cells to the min-heap
        for i in range(n):
            for j in range(m):
                if i in (0, n - 1) or j in (0, m - 1):
                    heapq.heappush(heap, (heightMap[i][j], i, j))
                    visited[i][j] = True

        water = 0
        # Directions for exploring neighbors: up, down, left, right
        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        while heap:
            h, x, y = heapq.heappop(heap)

            for dx, dy in dirs:
                nx, ny = x + dx, y + dy

                if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
                    visited[nx][ny] = True
                    nh = heightMap[nx][ny]
                    # If neighbor is lower than current wall height, it traps water
                    if nh < h:
                        water += h - nh
                    # The new wall height is the max of the current wall and the neighbor's height
                    heapq.heappush(heap, (max(h, nh), nx, ny))

        return water

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
        ([[1,4,3,1,3,2],[3,2,1,3,2,4],[2,3,3,2,3,1]], 4),
        ([[3,3,3,3,3],[3,2,2,2,3],[3,2,1,2,3],[3,2,2,2,3],[3,3,3,3,3]], 10),
        ([[12,13,1,12],[13,4,13,12],[13,8,10,12],[12,13,12,12],[13,13,13,13]], 14),
        ([[]], 0),
        ([[1]], 0),
    ]

    test_solution(sol.trapRainWater, test_cases)

"""
Dry Run Example:
---------------
Input: heightMap = [[1,3],[2,1]] -> Simplified for brevity
n=2, m=2

1. Init:
   - visited = [[F,F],[F,F]]
   - heap = []
   - Add borders: (1,0,0), (3,0,1), (2,1,0), (1,1,1) -> heap becomes [(1,0,0), (1,1,1), (2,1,0), (3,0,1)]
   - visited = [[T,T],[T,T]] -> All are borders, so all are visited.
   - water = 0

2. Loop:
   - heap is not empty.
   - Pop (1,0,0). h=1, x=0, y=0.
   - Neighbors of (0,0): (0,1) and (1,0). Both are already visited.
   - Pop (1,1,1). h=1, x=1, y=1.
   - Neighbors of (1,1): (0,1) and (1,0). Both are already visited.
   - ... and so on.

This example is trivial as there are no inner cells. Let's take a 3x3.
Input: [[3,3,3],[3,1,3],[3,3,3]]

1. Init:
   - heap = [(3,0,0), (3,0,1), (3,0,2), (3,1,0), (3,1,2), (3,2,0), (3,2,1), (3,2,2)]
   - visited has all borders True, center (1,1) is False.
   - water = 0

2. Loop 1:
   - Pop (3,0,0). h=3, x=0, y=0.
   - Neighbors: (0,1) [visited], (1,0) [visited].

3. ... (many pops of height 3 with no unvisited neighbors) ...

4. Let's say we pop (3,1,0). h=3, x=1, y=0.
   - Neighbors: (0,0)[v], (2,0)[v], (1,1)[not visited].
   - Process (nx=1, ny=1):
     - visited[1][1] = True
     - nh = heightMap[1][1] = 1.
     - nh (1) < h (3) -> water += 3 - 1 = 2.
     - Push (max(h,nh), 1, 1) -> (max(3,1), 1, 1) -> (3,1,1) to heap.

5. Now heap contains (3,1,1) and other border cells of height 3.
   - Eventually, all border cells are popped.
   - Pop (3,1,1). h=3, x=1, y=1.
   - Neighbors: (0,1), (2,1), (1,0), (1,2). All are visited.

6. Heap becomes empty.

Final water = 2.
"""
