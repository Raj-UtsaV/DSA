"""Canonical solution metadata.

Problem Number: 547
Problem Title: Number of Provinces
Platform: LeetCode
Difficulty: Medium
Official Platform Topics: Depth-First Search, Breadth-First Search, Union-Find, Graph Theory
Study Tags: Connected components, Disjoint Set Union
Canonical URL: https://leetcode.com/problems/number-of-provinces/
"""

"""
Problem Description:
--------------------
[problem:] Number of Provinces
[link:] https://leetcode.com/problems/number-of-provinces/
[description:] Given an n x n matrix isConnected where isConnected[i][j] = 1 if the ith city and the jth city are directly connected, and isConnected[i][j] = 0 otherwise.
Return the total number of provinces.
A province is a group of directly or indirectly connected cities and no other cities outside of the group.

Example:
--------
Input: adj = [[1,1,0],[1,1,0],[0,0,1]], V = 3
Output: 2
"""

#!IDEA
"""
The problem asks for the number of connected components in the graph.
We can use the Disjoint Set Union (DSU) data structure.

--- Solution: Disjoint Set Union ---

*   **State**:
    -   `ds`: An instance of the DisjointSet class handling `V` nodes.

*   **Core Logic**:
    1.  Initialize DSU with `V` nodes.
    2.  Iterate through the adjacency matrix `adj`.
    3.  If `adj[i][j] == 1`, perform `union_by_size(i, j)` to merge the sets containing nodes `i` and `j`.
    4.  After processing all edges, iterate through all nodes from `0` to `V-1`.
    5.  Count how many nodes are their own ultimate parent (`ds.find_ultimate_parent(i) == i`). Each such node represents a unique component (province).

*   **Complexity**:
    -   Time Complexity: O(V^2) for iterating the matrix. DSU operations are nearly constant.
    -   Space Complexity: O(V) for the DSU structure.
"""

from reference.graphs.disjoint_set_union import DisjointSet
from typing import List

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        size = len(isConnected)
        ds = DisjointSet(size)
        for row in range(size):
            for column in range(row + 1, size):
                if isConnected[row][column]:
                    ds.union_by_size(row, column)
        return sum(
            ds.find_ultimate_parent(node) == node for node in range(size)
        )

# --- Testing System ---
def test_solution(func, test_cases):
    for idx, (input_val, expected) in enumerate(test_cases, 1):
        adj, V = input_val
        output = func(adj, V)
        if output == expected:
            print(f"Test case {idx}: ✅ Passed")
        else:
            print(f"Test case {idx}: ❌ Failed")
            print(f"  Input: adj={adj}, V={V}")
            print(f"  Output: {output}")
            print(f"  Expected: {expected}")

# --- Example Test Cases ---
if __name__ == "__main__":
    sol = Solution()
    test_cases = [
        (
            ([[1, 1, 0], [1, 1, 0], [0, 0, 1]], 3),
            2
        ),
        (
            ([[1, 0, 0], [0, 1, 0], [0, 0, 1]], 3),
            3
        ),
    ]

    test_solution(sol.numProvinces, test_cases)

"""
Dry Run Example:
---------------
Input: adj = [[1,1,0],[1,1,0],[0,0,1]], V = 3

1. Init DSU(3). Parent: [0, 1, 2, 3] (using 0-based indices mostly).

2. Process Matrix:
   - (0, 1) is 1 -> union(0, 1). Parent might become [0, 0, 2, 3].
   - (1, 0) is 1 -> union(1, 0). Already same.
   - (2, 2) is 1 -> union(2, 2). No change.

3. Count Provinces:
   - i=0: find(0) == 0? Yes. Count = 1.
   - i=1: find(1) == 0? No (parent is 0).
   - i=2: find(2) == 2? Yes. Count = 2.

Result: 2
"""
