"""Reusable reference: Disjoint Set Union with path compression and union heuristics.

Migrated from: Graph/Disjoint_set_union.py
"""

"""
Problem Description:
--------------------
Disjoint Set Union (DSU) Implementation
Link: N/A (General Data Structure)

Implement the Disjoint Set Union (DSU) data structure with Path Compression and Union by Rank/Size.
The DSU data structure allows for efficient management of a partition of a set into disjoint subsets.
It supports two primary operations:
1. Find: Determine which subset a particular element is in. This can be used for determining if two elements are in the same subset.
2. Union: Join two subsets into a single subset.

Example:
--------
Input: n=7, edges=[(1,2), (2,3), (4,5), (6,7), (5,6)], query=(3,7)
Output: False (Different Component)

Input: n=7, edges=[(1,2), (2,3), (4,5), (6,7), (5,6), (3,7)], query=(3,7)
Output: True (Same Component)
"""

#!IDEA
"""
Disjoint Set Union (DSU) is a graph data structure that tracks a set of elements partitioned into a number of disjoint (non-overlapping) subsets.

--- Approach: Path Compression and Union by Rank/Size ---

* State:
    - `parent`: An array where `parent[i]` stores the parent of node `i`. If `parent[i] == i`, then `i` is a root of a set.
    - `rank`: An array to store the approximate depth of the tree rooted at `i`. Used to keep the tree flat during union.
    - `size`: An array to store the number of elements in the set rooted at `i`. Alternative to rank for balancing.

* Core Logic:
    1.  **Initialization**:
        - Each node is its own parent initially (`parent[i] = i`).
        - Rank is initialized to 0.
        - Size is initialized to 1.

    2.  **Find Ultimate Parent (with Path Compression)**:
        - To find the representative (root) of the set containing `node`.
        - Recursively traverse up the `parent` array until `parent[node] == node`.
        - *Optimization (Path Compression)*: During the traversal, update `parent[node]` to point directly to the ultimate parent. This flattens the structure, making future operations faster.

    3.  **Union by Rank**:
        - Find the ultimate parents of `u` and `v` (`ulp_u`, `ulp_v`).
        - If they are already in the same set (`ulp_u == ulp_v`), do nothing.
        - Attach the shorter tree to the taller tree to minimize height increase.
        - If ranks are equal, attach one to the other and increment the rank of the new root.

    4.  **Union by Size**:
        - Similar to Union by Rank, but attaches the smaller set (by number of nodes) to the larger set.
        - Update the size of the new root.

* Complexity:
    - Time Complexity: O(4 * alpha(n)) which is nearly constant time O(1) on average for both Find and Union operations, where alpha is the inverse Ackermann function.
    - Space Complexity: O(n) to store `parent`, `rank`, and `size` arrays.
"""

class DisjointSet:
    def __init__(self, n):
        # 1-based indexing handling by size n + 1
        self.rank = [0] * (n + 1)
        self.parent = list(range(n + 1))
        self.size = [1] * (n + 1)

    def find_ultimate_parent(self, node):
        if node == self.parent[node]:
            return node
        # Path compression
        self.parent[node] = self.find_ultimate_parent(self.parent[node])
        return self.parent[node]

    def union_by_rank(self, u, v):
        ulp_u = self.find_ultimate_parent(u)
        ulp_v = self.find_ultimate_parent(v)

        if ulp_u == ulp_v:
            return

        if self.rank[ulp_u] < self.rank[ulp_v]:
            self.parent[ulp_u] = ulp_v
        elif self.rank[ulp_u] > self.rank[ulp_v]:
            self.parent[ulp_v] = ulp_u
        else:
            self.parent[ulp_v] = ulp_u
            self.rank[ulp_u] += 1

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
    def check_connectivity(self, n, edges, query, strategy="rank"):
        ds = DisjointSet(n)
        
        for u, v in edges:
            if strategy == "size":
                ds.union_by_size(u, v)
            else:
                ds.union_by_rank(u, v)
        
        return ds.find_ultimate_parent(query[0]) == ds.find_ultimate_parent(query[1])


# --- Testing System ---
def test_solution(func, test_cases):
    for idx, (input_val, expected) in enumerate(test_cases, 1):
        # Unpack input: n, edges, query, strategy
        n, edges, query, strategy = input_val
        output = func(n, edges, query, strategy)
        
        if output == expected:
            print(f"Test case {idx}: ✅ Passed")
        else:
            print(f"Test case {idx}: ❌ Failed")
            print(f"  Input: n={n}, edges={edges}, query={query}, strategy={strategy}")
            print(f"  Output: {output}")
            print(f"  Expected: {expected}")


# --- Example Test Cases ---
if __name__ == "__main__":
    sol = Solution()
    # Format: ((n, edges, query, strategy), expected_output)
    test_cases = [
        # Rank strategy tests
        ((7, [(1, 2), (2, 3), (4, 5), (6, 7), (5, 6)], (3, 7), "rank"), False),
        ((7, [(1, 2), (2, 3), (4, 5), (6, 7), (5, 6), (3, 7)], (3, 7), "rank"), True),
        
        # Size strategy tests
        ((7, [(1, 2), (2, 3), (4, 5), (6, 7), (5, 6)], (3, 7), "size"), False),
        ((7, [(1, 2), (2, 3), (4, 5), (6, 7), (5, 6), (3, 7)], (3, 7), "size"), True),
    ]
    
    test_solution(sol.check_connectivity, test_cases)


"""
Dry Run Example:
---------------
Input: n=7, edges=[(1,2), (2,3), (4,5), (6,7), (5,6)], query=(3,7), strategy="rank"

Initialize DisjointSet(7):
parent = [0, 1, 2, 3, 4, 5, 6, 7]
rank   = [0, 0, 0, 0, 0, 0, 0, 0]

1. union_by_rank(1, 2):
   ulp_1=1, ulp_2=2. ranks equal. parent[2]=1, rank[1]=1.
   parent: [0, 1, 1, 3, 4, 5, 6, 7]

... (intermediate unions) ...

Query: find(3) == find(7)?
- find(3) leads to root 1.
- find(7) leads to root 4.
- 1 != 4. Returns False.
"""