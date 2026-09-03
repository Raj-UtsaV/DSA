# 225 — Implement Stack using Queues

**Difficulty:** Easy

**LeetCode:** https://leetcode.com/problems/implement-stack-using-queues/

## Topics

Official LeetCode Topics:
- Stack
- Design
- Queue

Study Patterns:
- Stack and Queue Techniques

## Intuition

Rotating the queue after every insertion places the newest value at the front. That makes the queue's front behave like a stack's top.

## Approach

1. Append the new value to the queue.
2. Move every older value from the front to the back once.
3. Implement pop and top directly against the rotated queue front.

## Complexity

- Time: O(n) per push; O(1) per pop or top
- Space: O(n)

## Solution

[View Python solution](./solution.py)

## Interview Notes

- Recognize this problem when its constraints match the Stack and Queue Techniques pattern.
- Keep the core invariant explicit; updating state in the wrong order is a common source of errors.
- Check boundary-sized inputs before relying on the general iteration.

## Notion Notes

Detailed explanation, code walkthrough, dry run and diagrams:

Notion page: [https://app.notion.com/p/3d050eec34db8161bd6fff449743c1fd?pvs=204](https://app.notion.com/p/3d050eec34db8161bd6fff449743c1fd?pvs=204)
