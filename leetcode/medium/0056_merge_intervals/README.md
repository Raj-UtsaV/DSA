# 56 — Merge Intervals

**Difficulty:** Medium

**LeetCode:** https://leetcode.com/problems/merge-intervals/

## Topics

Official LeetCode Topics:
- Array
- Sorting
- Quicksort

Study Patterns:
- Interval Problems

## Intuition

A locally optimal choice for merge intervals leaves the greatest flexibility for the remaining input. Ordering the candidates makes that safe choice available at each step.

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

Notion page: [https://app.notion.com/p/3d050eec34db81df9b43dc63aea3ce81?pvs=204](https://app.notion.com/p/3d050eec34db81df9b43dc63aea3ce81?pvs=204)
