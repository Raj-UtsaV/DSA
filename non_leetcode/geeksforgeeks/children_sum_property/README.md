# Children Sum Property

**Difficulty:** Not reliably specified

**Platform:** GeeksforGeeks

**Problem:** https://www.geeksforgeeks.org/problems/children-sum-parent/1

## Topics

Study Topics:
- Tree Recursion

Study Patterns:
- Tree DFS and BFS

## Intuition

The result for children sum property follows from information collected while traversing the tree. Each node is processed once, with recursion or a queue preserving the required traversal order.

## Approach

1. Handle the empty-node base case.
2. Traverse the required child nodes and update or combine their information at the current node.
3. Return the value accumulated for the root or traversal output.

## Complexity

- Time: O(n)
- Space: O(h) recursion stack

## Solution

[View Python solution](./solution.py)

## Interview Notes

- Recognize this problem when its constraints match the Tree DFS and BFS pattern.
- Keep the core invariant explicit; updating state in the wrong order is a common source of errors.
- Check boundary-sized inputs before relying on the general iteration.

## Notion Notes

Detailed explanation, code walkthrough, dry run and diagrams:

Notion page: TODO
