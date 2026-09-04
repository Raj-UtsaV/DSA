# 845 — Longest Mountain in Array

**Difficulty:** Medium

**LeetCode:** https://leetcode.com/problems/longest-mountain-in-array/

## Topics

Official LeetCode Topics:
- Array
- Two Pointers
- Dynamic Programming
- Enumeration

Study Patterns:
- Increasing and decreasing runs

## Intuition

The implementation solves longest mountain in array by scanning the relevant input while maintaining the smallest state needed for the answer. Each item is incorporated once in the order required by the Increasing and decreasing runs technique.

## Approach

1. Initialize the state required by the Increasing and decreasing runs invariant.
2. Process each relevant input item and update the candidate result.
3. Return the accumulated or validated result after the scan completes.

## Complexity

- Time: O(n)
- Space: O(1)

## Solution

[View Python solution](./solution.py)

## Interview Notes

- Recognize this problem when its constraints match the Increasing and decreasing runs pattern.
- Keep the core invariant explicit; updating state in the wrong order is a common source of errors.
- Check boundary-sized inputs before relying on the general iteration.

## Notion Notes

Detailed explanation, code walkthrough, dry run and diagrams:

Notion page: https://app.notion.com/p/3d150eec34db816b9251cff0cbcb89ca?pvs=204
