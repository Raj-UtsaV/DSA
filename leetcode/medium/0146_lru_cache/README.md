# 146 — LRU Cache

**Difficulty:** Medium

**LeetCode:** https://leetcode.com/problems/lru-cache/

## Topics

Official LeetCode Topics:
- Hash Table
- Linked List
- Design
- Doubly-Linked List

Study Patterns:
- Eviction Policy

## Intuition

The cache must identify keys and update recency in constant average time. An ordered dictionary combines hash lookup with an order that moves recently accessed keys to the end and exposes the least-recent key at the front.

## Approach

1. Store cache entries in an ordered dictionary.
2. On access or update, move the key to the most-recent end.
3. After an insertion exceeds capacity, evict the first, least-recent entry.

## Complexity

- Time: O(1) average per get or put
- Space: O(capacity)

## Solution

[View Python solution](./solution.py)

## Interview Notes

- Recognize this problem when its constraints match the Eviction Policy pattern.
- Keep the core invariant explicit; updating state in the wrong order is a common source of errors.
- Check boundary-sized inputs before relying on the general iteration.

## Notion Notes

Detailed explanation, code walkthrough, dry run and diagrams:

Notion page: TODO
