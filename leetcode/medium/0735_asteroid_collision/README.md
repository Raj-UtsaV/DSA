# 735 — Asteroid Collision

**Difficulty:** Medium

**LeetCode:** https://leetcode.com/problems/asteroid-collision/

## Topics

Official LeetCode Topics:
- Array
- Stack
- Simulation

Study Patterns:
- Stack and Queue Techniques

## Intuition

The unresolved items in asteroid collision must be handled in a specific last-in or first-in order. The stack or queue stores exactly those pending items until they can be resolved.

## Approach

1. Initialize the stack or queue holding unresolved state.
2. Process each item, removing entries that the current item completes and adding those still pending.
3. Build or return the result from the final data-structure state.

## Complexity

- Time: O(n)
- Space: O(n)

## Solution

[View Python solution](./solution.py)

## Interview Notes

- Recognize this problem when its constraints match the Stack and Queue Techniques pattern.
- Keep the core invariant explicit; updating state in the wrong order is a common source of errors.
- Check boundary-sized inputs before relying on the general iteration.

## Notion Notes

Detailed explanation, code walkthrough, dry run and diagrams:

Notion page: https://app.notion.com/p/3d150eec34db8192b8bafb45222c50bf?pvs=204
