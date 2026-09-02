"""Reusable reference: Prim's minimum spanning tree algorithm.

Migrated from: Graph/Minium_SPanning_Tree.py
"""

"""
Problem Description:
--------------------
Minimum Spanning Tree (Prim's Algorithm)
Link: https://www.geeksforgeeks.org/problems/minimum-spanning-tree/1

Given a weighted, undirected, and connected graph of V vertices and E edges.
The task is to find the sum of weights of the edges of the Minimum Spanning Tree.

Example:
--------
Input: V = 3, edges = [[0, 1, 5], [1, 2, 3], [0, 2, 1]]
Output: 4
Explanation:
The edge 0-2 has weight 1.
The edge 1-2 has weight 3.
Total MST weight = 1 + 3 = 4.
"""

#!IDEA
"""
The problem asks for the Minimum Spanning Tree (MST) sum of a connected undirected graph.
We can use Prim's Algorithm, which is a greedy approach.

--- Solution: Prim's Algorithm ---

* State:
    - `pq`: A min-heap (priority queue) storing tuples of `(weight, node)`. This allows us to always
      pick the edge with the smallest weight connecting the currently visited set of nodes to the unvisited set.
    - `visited`: A boolean array to keep track of included nodes to avoid cycles.
    - `mst_sum`: Accumulator for the total weight of the MST.

* Core Logic:
    1.  **Initialization**:
        - Start with an arbitrary node (e.g., node 0).
        - Push `(0, 0)` to the priority queue (weight 0 to reach node 0).
        - Initialize `visited` array to False.

    2.  **Processing**:
        - While the priority queue is not empty:
            - Pop the element with the smallest weight: `(wt, node)`.
            - If `node` is already visited, skip it.
            - Mark `node` as visited.
            - Add `wt` to `mst_sum`.
            - Iterate through all neighbors of `node`. If a neighbor is not visited, push `(edge_weight, neighbor)` to the heap.

* Complexity:
    - Time Complexity: O(E * log E) or O(E * log V), where E is the number of edges and V is the number of vertices.
    - Space Complexity: O(E + V) for the adjacency list and the priority queue.
"""

from typing import List
import heapq

class Solution:
    def spanningTree(self, V: int, edges: List[List[int]]) -> int:
        # Create adjacency list
        adj = [[] for _ in range(V)]
        for u, v, w in edges:
            adj[u].append((v, w))
            adj[v].append((u, w))
        
        # Min-heap stores (weight, node)
        # Start with node 0 and weight 0
        pq = [(0, 0)]
        mst_sum = 0
        visited = [False] * V
        
        while pq:
            wt, node = heapq.heappop(pq)
            
            if visited[node]:
                continue
            
            visited[node] = True
            mst_sum += wt
            
            for neighbor, edge_weight in adj[node]:
                if not visited[neighbor]:
                    heapq.heappush(pq, (edge_weight, neighbor))
                    
        return mst_sum


# --- Testing System ---
def test_solution(func, test_cases):
    for idx, (input_val, expected) in enumerate(test_cases, 1):
        V, edges = input_val
        output = func(V, edges)
        if output == expected:
            print(f"Test case {idx}: ✅ Passed")
        else:
            print(f"Test case {idx}: ❌ Failed")
            print(f"  Input: V={V}, edges={edges}")
            print(f"  Output: {output}")
            print(f"  Expected: {expected}")


# --- Example Test Cases ---
if __name__ == "__main__":
    sol = Solution()
    test_cases = [
        ((3, [[0, 1, 5], [1, 2, 3], [0, 2, 1]]), 4),
        ((2, [[0, 1, 5]]), 5),
        ((4, [[0, 1, 1], [0, 2, 2], [0, 3, 2], [1, 2, 1]]), 4), # MST: 0-1(1), 1-2(1), 0-3(2) -> 1+1+2=4
    ]

    test_solution(sol.spanningTree, test_cases)

"""
Dry Run Example:
---------------
Input: V = 3, edges = [[0, 1, 5], [1, 2, 3], [0, 2, 1]]

1. Init:
   - adj = {0: [(1,5), (2,1)], 1: [(0,5), (2,3)], 2: [(1,3), (0,1)]}
   - pq = [(0, 0)]  # (weight, node)
   - visited = [F, F, F]
   - mst_sum = 0

2. Iteration 1:
   - Pop (0, 0). wt=0, node=0.
   - visited[0] = True.
   - mst_sum += 0 -> 0.
   - Neighbors of 0:
     - (1, 5): Push (5, 1)
     - (2, 1): Push (1, 2)
   - pq = [(1, 2), (5, 1)]

3. Iteration 2:
   - Pop (1, 2). wt=1, node=2.
   - visited[2] = True.
   - mst_sum += 1 -> 1.
   - Neighbors of 2:
     - (1, 3): Push (3, 1)
     - (0, 1): 0 is visited, skip.
   - pq = [(3, 1), (5, 1)]

4. Iteration 3:
   - Pop (3, 1). wt=3, node=1.
   - visited[1] = True.
   - mst_sum += 3 -> 4.
   - Neighbors of 1:
     - (0, 5): 0 visited, skip.
     - (2, 3): 2 visited, skip.
   - pq = [(5, 1)]

5. Iteration 4:
   - Pop (5, 1). wt=5, node=1.
   - 1 is already visited. Continue.
   - pq = []

6. Return mst_sum = 4.
"""