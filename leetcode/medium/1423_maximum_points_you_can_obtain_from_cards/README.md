# 1423 — Maximum Points You Can Obtain from Cards

**Difficulty:** Medium

**LeetCode:** https://leetcode.com/problems/maximum-points-you-can-obtain-from-cards/

## Topics

Official LeetCode Topics:
- Array
- Sliding Window
- Prefix Sum

Study Patterns:
- Sliding Window

## Intuition

Valid candidates for maximum points you can obtain from cards occupy contiguous ranges. A moving window reuses the previous range's state instead of recomputing counts for every start position.

## Approach

1. Expand the right boundary and add the new element to the window state.
2. Move the left boundary while the required condition is violated.
3. Update the answer from each valid window.

## Complexity

- Time: O(n)
- Space: O(k), for the maintained frequency state

## Solution

[View Python solution](./solution.py)

## Interview Notes

- Recognize this problem when its constraints match the Sliding Window pattern.
- Keep the core invariant explicit; updating state in the wrong order is a common source of errors.
- Check boundary-sized inputs before relying on the general iteration.

## Notion Notes

Detailed explanation, code walkthrough, dry run and diagrams:

Notion page: https://app.notion.com/p/3d150eec34db815ab996db22618f1dc3?pvs=204
