# Find Nth Root of M

**Difficulty:** Not reliably specified

**Platform:** Code360

**Problem:** https://www.naukri.com/code360/problems/nth-root-of-m_1062679

## Topics

Study Topics:
- Binary Search

Study Patterns:
- Binary Search

## Intuition

The candidate values for find nth root of m have an ordered or monotonic structure. Binary search can discard half of the remaining range after each comparison or feasibility check.

## Approach

1. Choose bounds that contain every possible answer.
2. Evaluate the midpoint using the implementation's comparison or feasibility condition.
3. Move the invalid boundary until the search converges, then return the surviving candidate.

## Complexity

- Time: O(n log m)
- Space: O(1)

## Solution

[View Python solution](./solution.py)

## Interview Notes

- Recognize this problem when its constraints match the Binary Search pattern.
- Keep the core invariant explicit; updating state in the wrong order is a common source of errors.
- Check boundary-sized inputs before relying on the general iteration.

## Notion Notes

Detailed explanation, code walkthrough, dry run and diagrams:

Notion page: TODO
