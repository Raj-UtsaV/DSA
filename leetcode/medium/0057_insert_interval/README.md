# 57 — Insert Interval

**Difficulty:** Medium

**LeetCode:** https://leetcode.com/problems/insert-interval/

## Topics

Official LeetCode Topics:
- Array

Study Patterns:
- Interval Problems

## Intuition

A locally optimal choice for insert interval leaves the greatest flexibility for the remaining input. Ordering the candidates makes that safe choice available at each step.

## Approach

1. Order candidates by the criterion used by the greedy invariant.
2. Accept a candidate when it is compatible with the choices already made.
3. Return the accumulated count, value, or selected arrangement.

## Complexity

- Time: O(n log n)
- Space: O(n) for Python's sorting machinery

## Solution

[View Python solution](./solution.py)

## Interview Notes

- Recognize this problem when its constraints match the Interval Problems pattern.
- Keep the core invariant explicit; updating state in the wrong order is a common source of errors.
- Check boundary-sized inputs before relying on the general iteration.

## Notion Notes

Detailed explanation, code walkthrough, dry run and diagrams:

Notion page: TODO
