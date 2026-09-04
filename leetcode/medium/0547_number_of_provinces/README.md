# 547 — Number of Provinces

**Difficulty:** Medium

**LeetCode:** https://leetcode.com/problems/number-of-provinces/

## Topics

Official LeetCode Topics:
- Depth-First Search
- Breadth-First Search
- Union-Find
- Graph Theory

Study Patterns:
- Graph Traversal and Connectivity
- Disjoint Set Union

## Intuition

Cities form an undirected graph, and each province is one connected component. Union-Find merges every directly connected pair, after which each remaining root represents one province.

## Approach

1. Initialize a disjoint-set node for every city.
2. Scan only the upper triangle of the symmetric adjacency matrix and union connected pairs.
3. Count nodes that are their own ultimate parent.

## Complexity

- Time: O(n² α(n))
- Space: O(n)

## Solution

[View Python solution](./solution.py)

## Interview Notes

- Recognize this as connected-component counting on an adjacency matrix.
- Scanning one triangle avoids processing every undirected edge twice.
- Count ultimate roots after all unions, not intermediate parent values.

## Notion Notes

Detailed explanation, code walkthrough, dry run and diagrams:

Notion page: https://app.notion.com/p/3d150eec34db81aa844ed062bee03bd0?pvs=204
