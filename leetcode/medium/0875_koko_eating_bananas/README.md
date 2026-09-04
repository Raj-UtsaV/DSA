# 875 — Koko Eating Bananas

**Difficulty:** Medium

**LeetCode:** https://leetcode.com/problems/koko-eating-bananas/

## Topics

Official LeetCode Topics:
- Array
- Binary Search

Study Patterns:
- Binary Search on Answer

## Intuition

If Koko can finish at a particular speed, every faster speed is also feasible. This monotonic feasibility condition allows binary search over speeds from `1` through the largest pile.

## Approach

1. Binary-search the candidate eating speed in `[1, max(piles)]`.
2. For each midpoint, sum `ceil(pile / speed)` across all piles.
3. Keep the midpoint when it finishes within `h` hours; otherwise discard it and all slower speeds.
4. Return the smallest feasible speed.

## Complexity

- Time: O(n log m), where `m` is the largest pile
- Space: O(1)

## Solution

[View Python solution](./solution.py)

## Interview Notes

- Look for a minimum feasible value with a monotonic yes/no predicate.
- Integer ceiling is computed as `(pile + speed - 1) // speed`.
- The lower bound must start at `1`; a speed of zero is invalid.
- Moving the feasible boundary to `speed` preserves a possible optimal answer.

## Notion Notes

Detailed explanation, code walkthrough, dry run and diagrams:

Notion page: https://app.notion.com/p/3d150eec34db81acbde5cc7356d80418?pvs=204
