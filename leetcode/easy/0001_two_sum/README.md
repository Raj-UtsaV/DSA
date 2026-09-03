# 1 — Two Sum

**Difficulty:** Easy

**LeetCode:** https://leetcode.com/problems/two-sum/

## Topics

Official LeetCode Topics:
- Array
- Hash Table

Study Patterns:
- Hashing and Frequency Counting

## Intuition

For each number, the required partner is `target - number`. A hash map of previously seen values lets us determine immediately whether that partner has already appeared.

## Approach

1. Scan the array once while storing each value and its index.
2. Before storing the current value, look for its complement in the map.
3. Return the earlier index and current index when the complement is found.

## Complexity

- Time: O(n)
- Space: O(n)

## Solution

[View Python solution](./solution.py)

## Interview Notes

- Recognize the complement-lookup pattern when a pair must reach a target.
- Check before inserting so the same element is never used twice.
- Duplicate values work because indices, rather than only membership, are stored.

## Notion Notes

Detailed explanation, code walkthrough, dry run and diagrams:

Notion page: [https://app.notion.com/p/3d050eec34db8159ace5dc8288b859f4?pvs=204](https://app.notion.com/p/3d050eec34db8159ace5dc8288b859f4?pvs=204)
