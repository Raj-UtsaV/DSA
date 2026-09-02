# Triplet Sum

**Difficulty:** Not reliably specified

**Platform:** Other

**Problem Source:** Unresolved

## Topics

Study Topics:
- Sorting
- Two Pointers

Study Patterns:
- Sorting and Partitioning
- Two Pointers

## Intuition

The relevant positions for triplet sum can be advanced monotonically. Two pointers avoid restarting a scan and, where applicable, update the input in place.

## Approach

1. Initialize pointers at the required ends or read/write positions.
2. Compare or classify the current values and move the pointer whose state is resolved.
3. Continue until the pointers meet or the scan ends, then return the result.

## Complexity

- Time: O(n²)
- Space: O(1) auxiliary space

## Solution

[View Python solution](./solution.py)

## Interview Notes

- Recognize this problem when its constraints match the Sorting and Partitioning pattern.
- Keep the core invariant explicit; updating state in the wrong order is a common source of errors.
- Check boundary-sized inputs before relying on the general iteration.

## Notion Notes

Detailed explanation, code walkthrough, dry run and diagrams:

Notion page: TODO
