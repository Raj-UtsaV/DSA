"""Canonical solution metadata.

Problem Number: Not applicable
Problem Title: M-Coloring Problem
Platform: Code360
Difficulty: Not reliably specified
Official Platform Topics: Not specified
Study Tags: Graph Coloring, Backtracking
Canonical URL: https://www.naukri.com/code360/problems/m-coloring-problem_981273
"""

"""
Problem Description:
--------------------
[problem:] M-Coloring Problem
[link:] https://www.naukri.com/code360/problems/m-coloring-problem_981273
[Brief description of the problem, input/output requirements, constraints, and examples]
Given an undirected graph and an integer M, determine if the graph can be colored
with at most M colors such that no two adjacent vertices have the same color.

Example:
--------
Input:
graph = [
    [0, 1, 1, 1],
    [1, 0, 1, 0],
    [1, 1, 0, 1],
    [1, 0, 1, 0]
],
m = 3
Output: True
"""

"""
#!IDEA
- Use backtracking:
  1. Try assigning a color (from 1 to M) to each vertex one by one.
  2. Before assigning, check if the color is safe (i.e., no adjacent vertex has the same color).
  3. If we can assign colors to all vertices without conflicts, return True.
  4. If no color works for a vertex, backtrack and try a different color for previous vertices.
- Time complexity: O(M^N), where N is the number of vertices. Pruning (the safe check) helps reduce the practical search space.
"""

class Solution:
    def graphColoring(self, graph, m):
        n = len(graph)
        color = [0]*n

        def is_safe(node,c):
            for k in range(n):
                if graph[node][k] == 1 and color[k] == c:
                    return False

            return True

        def backtrack(node):
            if node == n:
                return True

            for c in range(1,m+1):
                if is_safe(node,c):
                    color[node] = c
                    if backtrack(node+1):
                        return True
                    color[node] = 0

            return False

        return backtrack(0)


# --- Testing System ---
def test_solution(func, test_cases):
    for idx, (inputs, expected) in enumerate(test_cases, 1):
        graph, m = inputs
        output = func(graph, m)
        if output == expected:
            print(f"Test case {idx}: ✅ Passed")
        else:
            print(f"Test case {idx}: ❌ Failed")
            print(f"  Input: graph={graph}, m={m}")
            print(f"  Output: {output}")
            print(f"  Expected: {expected}")


# --- Example Test Cases ---
if __name__ == "__main__":
    sol = Solution()
    test_cases = [
        (
            (
                [
                    [0, 1, 1, 1],
                    [1, 0, 1, 0],
                    [1, 1, 0, 1],
                    [1, 0, 1, 0]
                ], 3
            ), True
        ),
        (
            (
                [
                    [0, 1, 1, 1],
                    [1, 0, 1, 0],
                    [1, 1, 0, 1],
                    [1, 0, 1, 0]
                ], 2
            ), False
        ),
        (
            (
                [
                    [0, 1, 1],
                    [1, 0, 1],
                    [1, 1, 0]
                ], 3
            ), True
        ),
        (
            (
                [
                    [0, 1, 1],
                    [1, 0, 1],
                    [1, 1, 0]
                ], 2
            ), False
        )
    ]

    test_solution(sol.graphColoring, test_cases)

#---Dry run---

"""
🎯 Start Coloring

└── #!backtrack(0)
    └── #?is_safe(node=0, color=1) ✅ True
        🎨 assign color[0] = 1
        └── #!backtrack(1)
            ├── #?is_safe(node=1, color=1) ❌ False
            └── #?is_safe(node=1, color=2) ✅ True
                🎨 assign color[1] = 2
                └── #!backtrack(2)
                    ├── #?is_safe(node=2, color=1) ❌ False
                    ├── #?is_safe(node=2, color=2) ❌ False
                    └── #?is_safe(node=2, color=3) ✅ True
                        🎨 assign color[2] = 3
                        └── #!backtrack(3)
                            ├── #?is_safe(node=3, color=1) ❌ False
                            └── #?is_safe(node=3, color=2) ✅ True
                                🎨 assign color[3] = 2
                                ✅ SUCCESS → All vertices colored: [1, 2, 3, 2]


"""
