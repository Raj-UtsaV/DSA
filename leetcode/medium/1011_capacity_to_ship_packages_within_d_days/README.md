# 1011 — Capacity To Ship Packages Within D Days

**Difficulty:** Medium

**LeetCode:** https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/

## Topics

Official LeetCode Topics:
- Array
- Binary Search

Study Patterns:
- Binary Search on Answer

## Intuition

The candidate values for capacity to ship packages within d days have an ordered or monotonic structure. Binary search can discard half of the remaining range after each comparison or feasibility check.

## Approach

1. Choose bounds that contain every possible answer.
2. Evaluate the midpoint using the implementation's comparison or feasibility condition.
3. Move the invalid boundary until the search converges, then return the surviving candidate.

## Complexity

- Time: O(n log R), where R is the searched answer range
- Space: O(1)

## Solution

[View Python solution](./solution.py)

## Interview Notes

- Recognize this problem when its constraints match the Binary Search on Answer pattern.
- Keep the core invariant explicit; updating state in the wrong order is a common source of errors.
- Check boundary-sized inputs before relying on the general iteration.

## Notion Notes

Detailed explanation, code walkthrough, dry run and diagrams:

Notion page: TODO
