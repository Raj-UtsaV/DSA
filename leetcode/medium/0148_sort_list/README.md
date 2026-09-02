# 148 — Sort List

**Difficulty:** Medium

**LeetCode:** https://leetcode.com/problems/sort-list/

## Topics

Official LeetCode Topics:
- Linked List
- Two Pointers
- Divide and Conquer
- Sorting
- Merge Sort

Study Patterns:
- Linked-List Pointer Techniques
- Sorting and Partitioning

## Intuition

The linked structure in sort list can be handled by coordinating a small number of pointers. Their relative movement exposes the required position or permits local rewiring without an auxiliary collection.

## Approach

1. Initialize pointers at the positions required by the invariant.
2. Advance or rewire them in the order used by the canonical implementation.
3. Return the located node or updated list once the stopping condition is reached.

## Complexity

- Time: O(n log n)
- Space: O(log n) recursion stack

## Solution

[View Python solution](./solution.py)

## Interview Notes

- Recognize this problem when its constraints match the Linked-List Pointer Techniques pattern.
- Keep the core invariant explicit; updating state in the wrong order is a common source of errors.
- Check boundary-sized inputs before relying on the general iteration.

## Notion Notes

Detailed explanation, code walkthrough, dry run and diagrams:

Notion page: TODO
