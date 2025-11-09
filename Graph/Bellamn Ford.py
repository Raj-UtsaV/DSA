"""
Problem Description:
--------------------
[problem:] Bellman-Ford Algorithm
[link:] https://www.geeksforgeeks.org/problems/bellman-ford-graph-algorithm/1
[description:] Given a weighted, directed graph with `V` vertices and `E` edges, and a source
vertex `src`, find the shortest paths from the source to all other vertices. The algorithm
must also be able to detect if the graph contains a negative-weight cycle.

Example:
--------
Input: V = 6, edges = [[0,1,5],[1,2,-2],[1,5,-3],[2,4,3],[3,2,6],[3,4,-2],[5,3,1]], src = 0
Output: [0, 5, 3, 4, 1, 2]

"""

#!IDEA
"""
The Bellman-Ford algorithm is used to find the shortest paths from a single source vertex to all
other vertices in a weighted digraph. It is slower than Dijkstra's algorithm but more versatile,
as it can handle graphs with negative edge weights.

--- Solution: Bellman-Ford Algorithm ---

*   **State**:
    -   `dist`: An array of size `V`, where `dist[i]` stores the shortest distance found so far
        from the source vertex `src` to vertex `i`.

*   **Core Logic**:
    1.  **Initialization**:
        -   Initialize the `dist` array with a large value (infinity) for all vertices, representing
            that they are unreachable.
        -   Set the distance to the source vertex `dist[src]` to 0.

    2.  **Relaxation of Edges**:
        -   The core of the algorithm is to iteratively relax the edges. In a graph with `V` vertices,
            the longest possible simple path (without cycles) can have at most `V-1` edges.
        -   Therefore, we repeat the relaxation step `V-1` times.
        -   In each iteration, we loop through all edges `(u, v)` with weight `wt`.
        -   For each edge, we check if the path through `u` is shorter than the known path to `v`.
            That is, if `dist[u] + wt < dist[v]`.
        -   If it is, we update `dist[v] = dist[u] + wt`.

    3.  **Negative Cycle Detection**:
        -   After `V-1` iterations, if there are no negative-weight cycles, the `dist` array holds
            the shortest path distances.
        -   To check for negative cycles, we perform one more (the V-th) iteration of relaxation.
        -   If we can still find a shorter path for any vertex `v` (i.e., if `dist[u] + wt < dist[v]`
            is true for any edge), it means the graph contains a negative-weight cycle. This is because
            the path length can be infinitely reduced by traversing the cycle.

*   **Result**:
    -   If a negative cycle is detected during the V-th iteration, it's impossible to find the "true"
        shortest paths. In this case, we return an indicator, such as `[-1]`.
    -   If no negative cycle is found, the `dist` array contains the shortest distances from the
        source to all other vertices.

*   **Complexity**:
    -   Time Complexity: O(V * E), where V is the number of vertices and E is the number of edges.
        The algorithm iterates through all E edges, and this is done V times.
    -   Space Complexity: O(V) for the `dist` array.
"""

from typing import List

class Solution:
    def bellmanFord(self, V: int, edges: List[List[int]], src: int) -> List[int]:
        # 1. Initialize distances
        dist = [int(1e8)] * V
        dist[src] = 0

        # 2. Relax edges V-1 times
        for _ in range(V - 1):
            for edge in edges:
                u, v, wt = edge
                if dist[u] != int(1e8) and dist[u] + wt < dist[v]:
                    dist[v] = dist[u] + wt

        # 3. Check for negative-weight cycles
        for edge in edges:
            u, v, wt = edge
            if dist[u] != int(1e8) and dist[u] + wt < dist[v]:
                # Negative cycle detected
                return [-1]

        # 4. Return the result
        return dist

# --- Testing System ---
def test_solution(func, test_cases):
    for idx, (input_val, expected) in enumerate(test_cases, 1):
        V, edges, src = input_val
        output = func(V, edges, src)
        if output == expected:
            print(f"Test case {idx}: ✅ Passed")
        else:
            print(f"Test case {idx}: ❌ Failed")
            print(f"  Input: V={V}, Edges={edges}, Src={src}")
            print(f"  Output:   {output}")
            print(f"  Expected: {expected}")

# --- Example Test Cases ---
if __name__ == "__main__":
    sol = Solution()
    test_cases = [
        (
            (6, [[0,1,5],[1,2,-2],[1,5,-3],[2,4,3],[3,2,6],[3,4,-2],[5,3,1]], 0),
            [0, 5, 3, 3, 1, 2]
        ),
        (
            (3, [[0,1,5],[1,2,1],[2,0,-7]], 0),
            [-1]
        ),
        (
            (2, [[0,1,9]], 1),
            [100000000, 0]
        ),
    ]

    test_solution(sol.bellmanFord, test_cases)

"""
Dry Run Example:
---------------
Input: V=4, edges=[[0,1,4],[0,2,2],[1,3,3],[2,1,1],[2,3,5]], src=0

1. Init: dist = [0, 1e8, 1e8, 1e8]

2. Relaxation (i=0):
   - (0,1,4): dist[1] = min(1e8, 0+4) = 4
   - (0,2,2): dist[2] = min(1e8, 0+2) = 2
   - dist is now [0, 4, 2, 1e8]

3. Relaxation (i=1):
   - (2,1,1): dist[1] = min(4, 2+1) = 3
   - (1,3,3): dist[3] = min(1e8, 3+3) = 6
   - (2,3,5): dist[3] = min(6, 2+5) = 6
   - dist is now [0, 3, 2, 6]

4. Relaxation (i=2):
   - No changes occur. dist remains [0, 3, 2, 6]

5. Negative Cycle Check:
   - One more pass over all edges. No `dist[u] + wt < dist[v]` condition is met.
   - No negative cycle.

Result: Return [0, 3, 2, 6]
"""
