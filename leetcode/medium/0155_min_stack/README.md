# 155 — Min Stack

**Difficulty:** Medium

**LeetCode:** https://leetcode.com/problems/min-stack/

## Topics

Official LeetCode Topics:
- Stack
- Design

Study Patterns:
- Stack and Queue Techniques

## Intuition

Each stack entry stores both its value and the minimum at that depth. The current minimum is therefore always available at the top without rescanning earlier values.

## Approach

1. Push each value together with the smaller of itself and the previous minimum.
2. Pop both pieces of state together.
3. Read the value or minimum directly from the top pair.

## Complexity

- Time: O(1) per operation
- Space: O(n)

## Solution

[View Python solution](./solution.py)

## Interview Notes

- Recognize this problem when its constraints match the Stack and Queue Techniques pattern.
- Keep the core invariant explicit; updating state in the wrong order is a common source of errors.
- Check boundary-sized inputs before relying on the general iteration.

## Notion Notes

Detailed explanation, code walkthrough, dry run and diagrams:

Notion page: TODO
