# 76 — Minimum Window Substring

**Difficulty:** Hard

**LeetCode:** https://leetcode.com/problems/minimum-window-substring/

## Topics

Official LeetCode Topics:
- Hash Table
- String
- Sliding Window

Study Patterns:
- Hashing and Frequency Counting

## Intuition

The information needed for minimum window substring can be summarized by values already seen. A hash-based lookup avoids repeatedly scanning earlier input.

## Approach

1. Create the required value-to-state or frequency mapping.
2. Scan the input, checking the map before or while updating the current value's entry.
3. Return the result as soon as its lookup condition is met, or after the scan completes.

## Complexity

- Time: O(n + m)
- Space: O(k), where k is the number of tracked characters

## Solution

[View Python solution](./solution.py)

## Interview Notes

- Recognize this problem when its constraints match the Hashing and Frequency Counting pattern.
- Keep the core invariant explicit; updating state in the wrong order is a common source of errors.
- Check boundary-sized inputs before relying on the general iteration.

## Notion Notes

Detailed explanation, code walkthrough, dry run and diagrams:

Notion page: TODO
