# 1358 — Number of Substrings Containing All Three Characters

**Difficulty:** Medium

**LeetCode:** https://leetcode.com/problems/number-of-substrings-containing-all-three-characters/

## Topics

Official LeetCode Topics:
- Hash Table
- String
- Sliding Window

Study Patterns:
- Sliding Window

## Intuition

Valid candidates for number of substrings containing all three characters occupy contiguous ranges. A moving window reuses the previous range's state instead of recomputing counts for every start position.

## Approach

1. Expand the right boundary and add the new element to the window state.
2. Move the left boundary while the required condition is violated.
3. Update the answer from each valid window.

## Complexity

- Time: O(n)
- Space: O(k), for the maintained frequency state

## Solution

[View Python solution](./solution.py)

## Interview Notes

- Recognize this problem when its constraints match the Sliding Window pattern.
- Keep the core invariant explicit; updating state in the wrong order is a common source of errors.
- Check boundary-sized inputs before relying on the general iteration.

## Notion Notes

Detailed explanation, code walkthrough, dry run and diagrams:

Notion page: https://app.notion.com/p/3d150eec34db81169a1fda1d8c9a8e17?pvs=204
