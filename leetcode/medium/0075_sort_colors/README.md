# 75 — Sort Colors

**Difficulty:** Medium

**LeetCode:** https://leetcode.com/problems/sort-colors/

## Topics

Official LeetCode Topics:
- Array
- Two Pointers
- Sorting
- Quicksort
- Bubble Sort

Study Patterns:
- Sorting and Partitioning

## Intuition

The implementation solves sort colors by scanning the relevant input while maintaining the smallest state needed for the answer. Each item is incorporated once in the order required by the Sorting and Partitioning technique.

## Approach

1. Initialize the state required by the Sorting and Partitioning invariant.
2. Process each relevant input item and update the candidate result.
3. Return the accumulated or validated result after the scan completes.

## Complexity

- Time: O(n)
- Space: O(n)

## Solution

[View Python solution](./solution.py)

## Interview Notes

- Recognize this problem when its constraints match the Sorting and Partitioning pattern.
- Keep the core invariant explicit; updating state in the wrong order is a common source of errors.
- Check boundary-sized inputs before relying on the general iteration.

## Notion Notes

Detailed explanation, code walkthrough, dry run and diagrams:

Notion page: https://app.notion.com/p/3d050eec34db81d7bf27cb323d8dc12b?pvs=204
