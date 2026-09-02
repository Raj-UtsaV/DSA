# 2 — Add Two Numbers

**Difficulty:** Medium

**LeetCode:** https://leetcode.com/problems/add-two-numbers/

## Topics

Official LeetCode Topics:
- Linked List
- Math
- Recursion

Study Patterns:
- Carry Propagation

## Intuition

The implementation solves add two numbers by scanning the relevant input while maintaining the smallest state needed for the answer. Each item is incorporated once in the order required by the Carry Propagation technique.

## Approach

1. Initialize the state required by the Carry Propagation invariant.
2. Process each relevant input item and update the candidate result.
3. Return the accumulated or validated result after the scan completes.

## Complexity

- Time: O(max(m, n))
- Space: O(1) auxiliary space, excluding the result list

## Solution

[View Python solution](./solution.py)

## Interview Notes

- Recognize this problem when its constraints match the Carry Propagation pattern.
- Keep the core invariant explicit; updating state in the wrong order is a common source of errors.
- Check boundary-sized inputs before relying on the general iteration.

## Notion Notes

Detailed explanation, code walkthrough, dry run and diagrams:

Notion page: TODO
