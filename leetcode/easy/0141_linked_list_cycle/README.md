# 141 — Linked List Cycle

**Difficulty:** Easy

**LeetCode:** https://leetcode.com/problems/linked-list-cycle/

## Topics

Official LeetCode Topics:
- Hash Table
- Linked List
- Two Pointers
- Floyd's Cycle Finding Algorithm

Study Patterns:
- Fast/Slow Pointers

## Intuition

The linked structure in linked list cycle can be handled by coordinating a small number of pointers. Their relative movement exposes the required position or permits local rewiring without an auxiliary collection.

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

- Recognize this problem when its constraints match the Fast/Slow Pointers pattern.
- Keep the core invariant explicit; updating state in the wrong order is a common source of errors.
- Check boundary-sized inputs before relying on the general iteration.

## Notion Notes

Detailed explanation, code walkthrough, dry run and diagrams:

Notion page: [https://app.notion.com/p/3d050eec34db8126a04aca0d42f1e6ae?pvs=204](https://app.notion.com/p/3d050eec34db8126a04aca0d42f1e6ae?pvs=204)
