# 503 — Next Greater Element II

**Difficulty:** Medium

**LeetCode:** https://leetcode.com/problems/next-greater-element-ii/

## Topics

Official LeetCode Topics:
- Array
- Stack
- Monotonic Stack

Study Patterns:
- Monotonic Stack and Queue

## Intuition

For next greater element ii, elements made irrelevant by a newer value never need to be reconsidered. A monotonic stack or deque retains only useful candidates in order.

## Approach

1. Scan the input once while maintaining the required monotonic order.
2. Pop candidates that the current value resolves or dominates.
3. Use the remaining boundary information to update the answer, then add the current value.

## Complexity

- Time: O(n)
- Space: O(n)

## Solution

[View Python solution](./solution.py)

## Interview Notes

- Recognize this problem when its constraints match the Monotonic Stack and Queue pattern.
- Keep the core invariant explicit; updating state in the wrong order is a common source of errors.
- Check boundary-sized inputs before relying on the general iteration.

## Notion Notes

Detailed explanation, code walkthrough, dry run and diagrams:

Notion page: TODO
