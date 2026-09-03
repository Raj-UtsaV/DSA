# 69 — Sqrt(x)

**Difficulty:** Easy

**LeetCode:** https://leetcode.com/problems/sqrtx/

## Topics

Official LeetCode Topics:
- Math
- Binary Search
- Newton's Method

Study Patterns:
- Binary Search on Answer

## Intuition

The candidate values for sqrt(x) have an ordered or monotonic structure. Binary search can discard half of the remaining range after each comparison or feasibility check.

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

- Recognize this problem when its constraints match the Binary Search on Answer pattern.
- Keep the core invariant explicit; updating state in the wrong order is a common source of errors.
- Check boundary-sized inputs before relying on the general iteration.

## Notion Notes

Detailed explanation, code walkthrough, dry run and diagrams:

Notion page: [https://app.notion.com/p/3d050eec34db81528a1bc8541aa01ce1?pvs=204](https://app.notion.com/p/3d050eec34db81528a1bc8541aa01ce1?pvs=204)
