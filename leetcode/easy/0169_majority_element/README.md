# 169 — Majority Element

**Difficulty:** Easy

**LeetCode:** https://leetcode.com/problems/majority-element/

## Topics

Official LeetCode Topics:
- Array
- Hash Table
- Divide and Conquer
- Sorting
- Counting
- Boyer–Moore Majority Vote Algorithm

Study Patterns:
- Boyer-Moore Voting

## Intuition

The implementation solves majority element by scanning the relevant input while maintaining the smallest state needed for the answer. Each item is incorporated once in the order required by the Boyer-Moore Voting technique.

## Approach

1. Initialize the state required by the Boyer-Moore Voting invariant.
2. Process each relevant input item and update the candidate result.
3. Return the accumulated or validated result after the scan completes.

## Complexity

- Time: O(n)
- Space: O(1)

## Solution

[View Python solution](./solution.py)

## Interview Notes

- Recognize this problem when its constraints match the Boyer-Moore Voting pattern.
- Keep the core invariant explicit; updating state in the wrong order is a common source of errors.
- Check boundary-sized inputs before relying on the general iteration.

## Notion Notes

Detailed explanation, code walkthrough, dry run and diagrams:

Notion page: [https://app.notion.com/p/3d050eec34db8158b510f136cb6427fc?pvs=204](https://app.notion.com/p/3d050eec34db8158b510f136cb6427fc?pvs=204)
