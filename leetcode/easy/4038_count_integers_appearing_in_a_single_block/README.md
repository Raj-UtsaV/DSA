# 4038 — Count Integers Appearing in a Single Block

**Difficulty:** Easy

**LeetCode:** https://leetcode.com/problems/count-integers-appearing-in-a-single-block/

## Topics

Official LeetCode Topics:
- Array
- Hash Table

Study Patterns:
- Hashing and Frequency Counting

## Intuition

An integer is special only while all of its occurrences belong to its first contiguous block. When the same integer appears again immediately after a different value, it has started another block and can be marked permanently invalid.

## Approach

1. Keep a dictionary mapping every encountered integer to whether it is still special.
2. Mark a number as special on its first occurrence.
3. Ignore consecutive repetitions because they remain inside the same block.
4. Mark a number as not special when it reappears after another value.
5. Count the dictionary values that remain true.

## Complexity

- Time: O(n)
- Space: O(k), where `k` is the number of distinct integers

## Solution

[View Python solution](./solution.py)

## Interview Notes

- Compare with the previous element to detect the start of a new block.
- Once a number has appeared in multiple blocks, it can never become special again.
- A block-count dictionary is an equivalent solution: count each block start and count values having exactly one block.

## Notion Notes

Detailed explanation, code walkthrough and dry run:

Notion page: [https://app.notion.com/p/3d150eec34db8152b444fd8ec858e1ef?pvs=204](https://app.notion.com/p/3d150eec34db8152b444fd8ec858e1ef?pvs=204)
