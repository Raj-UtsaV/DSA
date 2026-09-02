"""Canonical solution metadata.

Problem Number: 1319
Problem Title: Number of Operations to Make Network Connected
Platform: LeetCode
Difficulty: Medium
Official Platform Topics: Depth-First Search, Breadth-First Search, Union-Find, Graph Theory
Study Tags: Connected components, Disjoint Set Union
Canonical URL: https://leetcode.com/problems/number-of-operations-to-make-network-connected/
"""

"""
Problem Description:
--------------------
[problem:] Number of Operations to Make Network Connected
[link:] https://leetcode.com/problems/number-of-operations-to-make-network-connected/
[description:] There are n computers numbered from 0 to n - 1 connected by ethernet cables connections forming a network where connections[i] = [a, b] represents a connection between computers a and b. Any computer can reach any other computer directly or indirectly through the network.

You are given an initial computer network connections. You can extract certain cables between two directly connected computers, and place them between any pair of disconnected computers to make them directly connected.

Return the minimum number of times you need to do this in order to make all the computers connected. If it is not possible, return -1.

Example:
--------
Input: n = 4, connections = [[0,1],[0,2],[1,2]]
Output: 1
Explanation: Remove cable between 1 and 2 and place between 1 and 3.
"""

#!IDEA
"""
To connect all `n` computers, we need at least `n - 1` cables. If the total number of connections is less than `n - 1`, it's impossible, so return -1.

If we have enough cables, we need to find the number of connected components in the graph. Let's say there are `k` connected components. To connect these `k` components together, we need `k - 1` cables. Since we already established we have enough total cables (>= n-1), we can definitely move the redundant cables to bridge these components.

--- Solution: Disjoint Set Union (DSU) ---

*   **State**:
    -   `ds`: An instance of the DisjointSet class handling `n` nodes.
    -   `extra_edges`: Counter for edges that connect two nodes already in the same component.

*   **Core Logic**:
    1.  Initialize DSU with `n` nodes.
    2.  Iterate through `connections`. For each edge `(u, v)`:
        -   If `u` and `v` are already in the same component, increment `extra_edges`.
        -   Otherwise, union `u` and `v`.
    3.  Count the number of connected components. A node `i` is a root of a component if `ds.find_ultimate_parent(i) == i`.
    4.  If `extra_edges >= components - 1`, return `components - 1`.
    5.  Otherwise, return -1.

*   **Complexity**:
    -   Time Complexity: O(E * alpha(n)) where E is the number of connections.
    -   Space Complexity: O(n) for DSU.
"""

from reference.graphs.disjoint_set_union import DisjointSet
from typing import List

class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        if len(connections) < n - 1:
            return -1

        ds = DisjointSet(n)
        extra_edges = 0
        for u, v in connections:
            if ds.find_ultimate_parent(u) == ds.find_ultimate_parent(v):
                extra_edges += 1
            else:
                ds.union_by_size(u, v)

        components = 0
        for i in range(n):
            if ds.find_ultimate_parent(i) == i:
                components += 1

        if extra_edges >= components - 1:
            return components - 1
        else:
            return -1

# --- Testing System ---
def test_solution(func, test_cases):
    for idx, (input_val, expected) in enumerate(test_cases, 1):
        n, connections = input_val
        output = func(n, connections)
        if output == expected:
            print(f"Test case {idx}: ✅ Passed")
        else:
            print(f"Test case {idx}: ❌ Failed")
            print(f"  Input: n={n}, connections={connections}")
            print(f"  Output: {output}")
            print(f"  Expected: {expected}")

# --- Example Test Cases ---
if __name__ == "__main__":
    sol = Solution()
    test_cases = [
        ((4, [[0,1],[0,2],[1,2]]), 1),
        ((6, [[0,1],[0,2],[0,3],[1,2],[1,3]]), 2),
        ((6, [[0,1],[0,2],[0,3],[1,2]]), -1),
    ]

    test_solution(sol.makeConnected, test_cases)

"""
Dry Run Example:
---------------
Input: n = 4, connections = [[0,1],[0,2],[1,2]]

1. Check base case: len(connections) = 3. n - 1 = 3. 3 >= 3. Continue.

2. Init DSU(4). Parent: [0, 1, 2, 3]. extra_edges = 0.

3. Process Connections:
   - (0, 1): find(0)=0, find(1)=1. Union(0, 1). Parent: [0, 0, 2, 3].
   - (0, 2): find(0)=0, find(2)=2. Union(0, 2). Parent: [0, 0, 0, 3].
   - (1, 2): find(1)=0, find(2)=0. Same parent. extra_edges += 1 -> 1.

4. Count Components:
   - i=0: parent[0]=0. Count=1.
   - i=1: parent[1]=0.
   - i=2: parent[2]=0.
   - i=3: parent[3]=3. Count=2.

   Components = 2.

5. Check:
   - Need components - 1 = 1 edge.
   - Have extra_edges = 1.
   - 1 >= 1 is True.
   - Return 1.
"""
