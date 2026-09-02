# 778 — Swim in Rising Water

**Difficulty:** Hard

**LeetCode:** https://leetcode.com/problems/swim-in-rising-water/

## Topics

Official LeetCode Topics:
- Array
- Binary Search
- Depth-First Search
- Breadth-First Search
- Union-Find
- Minimax
- Heap (Priority Queue)
- Matrix
- Dijkstra's Algorithm

Study Patterns:
- Shortest Path

## Intuition

The states in swim in rising water form a graph whose edges describe legal next moves. Processing states in distance or cost order ensures the first finalized value is optimal.

## Approach

1. Initialize the start state in the queue or priority queue.
2. Remove the next best state and relax each legal neighbor that improves its recorded value.
3. Stop at the target or return its finalized distance or cost.

## Complexity

- Time: O(n² log(n²))
- Space: O(n²)

## Solution

[View Python solution](./solution.py)

## Interview Notes

- Recognize this problem when its constraints match the Shortest Path pattern.
- Keep the core invariant explicit; updating state in the wrong order is a common source of errors.
- Check boundary-sized inputs before relying on the general iteration.

## Notion Notes

Detailed explanation, code walkthrough, dry run and diagrams:

Notion page: TODO
