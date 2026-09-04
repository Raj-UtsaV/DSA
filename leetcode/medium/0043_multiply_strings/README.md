# 43 — Multiply Strings

**Difficulty:** Medium

**LeetCode:** https://leetcode.com/problems/multiply-strings/

## Topics

Official LeetCode Topics:
- Math
- String
- Simulation

Study Patterns:
- Grade-school multiplication

## Intuition

The implementation solves multiply strings by scanning the relevant input while maintaining the smallest state needed for the answer. Each item is incorporated once in the order required by the Grade-school multiplication technique.

## Approach

1. Initialize the state required by the Grade-school multiplication invariant.
2. Process each relevant input item and update the candidate result.
3. Return the accumulated or validated result after the scan completes.

## Complexity

- Time: O(mn)
- Space: O(m + n)

## Solution

[View Python solution](./solution.py)

## Interview Notes

- Recognize this problem when its constraints match the Grade-school multiplication pattern.
- Keep the core invariant explicit; updating state in the wrong order is a common source of errors.
- Check boundary-sized inputs before relying on the general iteration.

## Notion Notes

Detailed explanation, code walkthrough, dry run and diagrams:

Notion page: [https://app.notion.com/p/3d050eec34db81a2b657f53e947e9e9b?pvs=204](https://app.notion.com/p/3d050eec34db81a2b657f53e947e9e9b?pvs=204)
