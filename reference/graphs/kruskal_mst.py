"""Reusable reference: Kruskal's minimum spanning tree algorithm.

Migrated from: Graph/mST_DSU.py
"""

"""
Problem Description:
--------------------
Minimum Spanning Tree (Kruskal's Algorithm)
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
The problem asks for the Minimum Spanning Tree (MST) sum.
We can use Kruskal's Algorithm, which sorts all edges by weight and adds them if they don't form a cycle.
Disjoint Set Union (DSU) is used to efficiently check for cycles and merge components.

--- Solution: Kruskal's Algorithm with DSU ---

* State:
    - `parent`: Array where parent[i] is the parent of node i.
    - `size`: Array to store the size of the component rooted at i.

* Core Logic:
    1.  Sort all edges by weight in ascending order.
    2.  Initialize DSU with V vertices.
    3.  Iterate through sorted edges:
        - For edge (u, v, w):
        - Find ultimate parents of u and v.
        - If they are different, they are in different components.
        - Union them and add w to mst_sum.
    4.  Return mst_sum.

* Complexity:
    - Time Complexity: O(E log E) or O(E log V) for sorting. DSU operations are nearly O(1).
    - Space Complexity: O(V) for DSU structures.
"""

from typing import List

class DisjointSet:
    def __init__(self, n):
        self.parent = list(range(n + 1))
        self.rank = [0] * (n + 1)
        self.size = [1] * (n + 1)

    def find_ultimate_parent(self, node):
        if node == self.parent[node]:
            return node
        self.parent[node] = self.find_ultimate_parent(self.parent[node])
        return self.parent[node]

    def union_by_size(self, u, v):
        ulp_u = self.find_ultimate_parent(u)
        ulp_v = self.find_ultimate_parent(v)

        if ulp_u == ulp_v:
            return

        if self.size[ulp_u] < self.size[ulp_v]:
            self.parent[ulp_u] = ulp_v
            self.size[ulp_v] += self.size[ulp_u]
        else:
            self.parent[ulp_v] = ulp_u
            self.size[ulp_u] += self.size[ulp_v]

class Solution:
    def spanningTree(self, V: int, edges: List[List[int]]) -> int:
        edges.sort(key=lambda x: x[2])  # Sort edges based on weight
        ds = DisjointSet(V)
        mst_sum = 0
        for u, v, w in edges:
            if ds.find_ultimate_parent(u) != ds.find_ultimate_parent(v):
                ds.union_by_size(u, v)
                mst_sum += w
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
