# 136 — Single Number

**Difficulty:** Easy

**LeetCode:** https://leetcode.com/problems/single-number/

## Topics

Official LeetCode Topics:
- Array
- Bit Manipulation

Study Patterns:
- Bit Manipulation

## Intuition

The implementation solves single number by scanning the relevant input while maintaining the smallest state needed for the answer. Each item is incorporated once in the order required by the Bit Manipulation technique.

## Approach

1. Initialize the state required by the Bit Manipulation invariant.
2. Process each relevant input item and update the candidate result.
3. Return the accumulated or validated result after the scan completes.

## Complexity

- Time: O(n)
- Space: O(1)

## Solution

[View Python solution](./solution.py)

## Interview Notes

- Recognize this problem when its constraints match the Bit Manipulation pattern.
- Keep the core invariant explicit; updating state in the wrong order is a common source of errors.
- Check boundary-sized inputs before relying on the general iteration.

## Notion Notes

Detailed explanation, code walkthrough, dry run and diagrams:

Notion page: [https://app.notion.com/p/3d050eec34db81029d25dedd67511138?pvs=204](https://app.notion.com/p/3d050eec34db81029d25dedd67511138?pvs=204)
