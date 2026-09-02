# 160 — Intersection of Two Linked Lists

**Difficulty:** Easy

**LeetCode:** https://leetcode.com/problems/intersection-of-two-linked-lists/

## Topics

Official LeetCode Topics:
- Hash Table
- Linked List
- Two Pointers

Study Patterns:
- Linked-List Pointer Techniques

## Intuition

The linked structure in intersection of two linked lists can be handled by coordinating a small number of pointers. Their relative movement exposes the required position or permits local rewiring without an auxiliary collection.

## Approach

1. Initialize pointers at the positions required by the invariant.
2. Advance or rewire them in the order used by the canonical implementation.
3. Return the located node or updated list once the stopping condition is reached.

## Complexity

- Time: O(n)
- Space: O(1)

## Solution

[View Python solution](./solution.py)

## Interview Notes

- Recognize this problem when its constraints match the Linked-List Pointer Techniques pattern.
- Keep the core invariant explicit; updating state in the wrong order is a common source of errors.
- Check boundary-sized inputs before relying on the general iteration.

## Notion Notes

Detailed explanation, code walkthrough, dry run and diagrams:

Notion page: TODO
