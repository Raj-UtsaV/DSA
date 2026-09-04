# 417 — Pacific Atlantic Water Flow

**Difficulty:** Medium

**LeetCode:** https://leetcode.com/problems/pacific-atlantic-water-flow/

## Topics

Official LeetCode Topics:
- Array
- Depth-First Search
- Breadth-First Search
- Matrix

Study Patterns:
- Graph Traversal and Connectivity

## Intuition

The input for pacific atlantic water flow represents connectivity between graph elements. Grouping reachable or unioned elements turns the requested result into a component-level calculation.

## Approach

1. Initialize the graph traversal or disjoint-set state for every element.
2. Process each relevant connection and merge or visit the connected endpoints.
3. Derive the result from the final connected components.

## Complexity

- Time: O(rows × columns)
- Space: O(rows × columns)

## Solution

[View Python solution](./solution.py)

## Interview Notes

- Recognize this problem when its constraints match the Graph Traversal and Connectivity pattern.
- Keep the core invariant explicit; updating state in the wrong order is a common source of errors.
- Check boundary-sized inputs before relying on the general iteration.

## Notion Notes

Detailed explanation, code walkthrough, dry run and diagrams:

Notion page: https://app.notion.com/p/3d150eec34db8121b30ff1837bd4a8ad?pvs=204
