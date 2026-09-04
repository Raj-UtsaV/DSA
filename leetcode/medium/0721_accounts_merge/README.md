# 721 — Accounts Merge

**Difficulty:** Medium

**LeetCode:** https://leetcode.com/problems/accounts-merge/

## Topics

Official LeetCode Topics:
- Array
- Hash Table
- String
- Depth-First Search
- Breadth-First Search
- Union-Find
- Sorting

Study Patterns:
- Disjoint Set Union

## Intuition

The input for accounts merge represents connectivity between graph elements. Grouping reachable or unioned elements turns the requested result into a component-level calculation.

## Approach

1. Initialize the graph traversal or disjoint-set state for every element.
2. Process each relevant connection and merge or visit the connected endpoints.
3. Derive the result from the final connected components.

## Complexity

- Time: O(A α(A) + E log E)
- Space: O(A + E)

## Solution

[View Python solution](./solution.py)

## Interview Notes

- Recognize this problem when its constraints match the Disjoint Set Union pattern.
- Keep the core invariant explicit; updating state in the wrong order is a common source of errors.
- Check boundary-sized inputs before relying on the general iteration.

## Notion Notes

Detailed explanation, code walkthrough, dry run and diagrams:

Notion page: https://app.notion.com/p/3d150eec34db81359ed4fa038bd8b38a?pvs=204
