# Check if an Array Is Sorted

**Difficulty:** Easy

**Platform:** GeeksforGeeks

**Problem:** https://www.geeksforgeeks.org/problems/check-if-an-array-is-sorted0701/1

## Topics

Study Topics:
- Array

Study Patterns:
- Array

## Intuition

The implementation solves check if an array is sorted by scanning the relevant input while maintaining the smallest state needed for the answer. Each item is incorporated once in the order required by the Array technique.

## Approach

1. Initialize the state required by the Array invariant.
2. Process each relevant input item and update the candidate result.
3. Return the accumulated or validated result after the scan completes.

## Complexity

- Time: O(n log n)
- Space: O(n) for Python's sorting machinery

## Solution

[View Python solution](./solution.py)

## Interview Notes

- Recognize this problem when its constraints match the Array pattern.
- Keep the core invariant explicit; updating state in the wrong order is a common source of errors.
- Check boundary-sized inputs before relying on the general iteration.

## Notion Notes

Detailed explanation, code walkthrough, dry run and diagrams:

Notion page: TODO
