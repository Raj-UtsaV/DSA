# 33 — Search in Rotated Sorted Array

**Difficulty:** Medium

**LeetCode:** https://leetcode.com/problems/search-in-rotated-sorted-array/

## Topics

Official LeetCode Topics:
- Array
- Binary Search

Study Patterns:
- Binary Search

## Intuition

The candidate values for search in rotated sorted array have an ordered or monotonic structure. Binary search can discard half of the remaining range after each comparison or feasibility check.

## Approach

1. Choose bounds that contain every possible answer.
2. Evaluate the midpoint using the implementation's comparison or feasibility condition.
3. Move the invalid boundary until the search converges, then return the surviving candidate.

## Complexity

- Time: O(log n)
- Space: O(1)

## Solution

[View Python solution](./solution.py)

## Interview Notes

- Recognize this problem when its constraints match the Binary Search pattern.
- Keep the core invariant explicit; updating state in the wrong order is a common source of errors.
- Check boundary-sized inputs before relying on the general iteration.

## Notion Notes

Detailed explanation, code walkthrough, dry run and diagrams:

Notion page: [https://app.notion.com/p/3d050eec34db817492ddd232ca341c6a?pvs=204](https://app.notion.com/p/3d050eec34db817492ddd232ca341c6a?pvs=204)
