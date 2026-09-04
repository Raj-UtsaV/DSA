# 2300 — Successful Pairs of Spells and Potions

**Difficulty:** Medium

**LeetCode:** https://leetcode.com/problems/successful-pairs-of-spells-and-potions/

## Topics

Official LeetCode Topics:
- Array
- Two Pointers
- Binary Search
- Sorting

Study Patterns:
- Binary Search

## Intuition

The candidate values for successful pairs of spells and potions have an ordered or monotonic structure. Binary search can discard half of the remaining range after each comparison or feasibility check.

## Approach

1. Choose bounds that contain every possible answer.
2. Evaluate the midpoint using the implementation's comparison or feasibility condition.
3. Move the invalid boundary until the search converges, then return the surviving candidate.

## Complexity

- Time: O(m log m + n log m)
- Space: O(1) auxiliary space, excluding output

## Solution

[View Python solution](./solution.py)

## Interview Notes

- Recognize this problem when its constraints match the Binary Search pattern.
- Keep the core invariant explicit; updating state in the wrong order is a common source of errors.
- Check boundary-sized inputs before relying on the general iteration.

## Notion Notes

Detailed explanation, code walkthrough, dry run and diagrams:

Notion page: https://app.notion.com/p/3d150eec34db81e6863af2d36ed3b7cc?pvs=204
