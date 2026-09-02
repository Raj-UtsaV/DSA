# Number of NGEs to the Right

**Difficulty:** Not reliably specified

**Platform:** GeeksforGeeks

**Problem:** https://www.geeksforgeeks.org/problems/number-of-nges-to-the-right/1

## Topics

Study Topics:
- Array
- Queries

Study Patterns:
- Array
- Queries

## Intuition

The implementation solves number of nges to the right by scanning the relevant input while maintaining the smallest state needed for the answer. Each item is incorporated once in the order required by the Array technique.

## Approach

1. Initialize the state required by the Array invariant.
2. Process each relevant input item and update the candidate result.
3. Return the accumulated or validated result after the scan completes.

## Complexity

- Time: O(qn)
- Space: O(1) auxiliary space, excluding output

## Solution

[View Python solution](./solution.py)

## Interview Notes

- Recognize this problem when its constraints match the Array pattern.
- Keep the core invariant explicit; updating state in the wrong order is a common source of errors.
- Check boundary-sized inputs before relying on the general iteration.

## Notion Notes

Detailed explanation, code walkthrough, dry run and diagrams:

Notion page: TODO
