# Page Faults in LRU

**Difficulty:** Not reliably specified

**Platform:** GeeksforGeeks

**Problem:** https://www.geeksforgeeks.org/problems/page-faults-in-lru5603/1

## Topics

Study Topics:
- LRU Simulation

Study Patterns:
- LRU Simulation

## Intuition

The implementation solves page faults in lru by scanning the relevant input while maintaining the smallest state needed for the answer. Each item is incorporated once in the order required by the LRU Simulation technique.

## Approach

1. Initialize the state required by the LRU Simulation invariant.
2. Process each relevant input item and update the candidate result.
3. Return the accumulated or validated result after the scan completes.

## Complexity

- Time: O(np), where p is the cache capacity
- Space: O(p)

## Solution

[View Python solution](./solution.py)

## Interview Notes

- Recognize this problem when its constraints match the LRU Simulation pattern.
- Keep the core invariant explicit; updating state in the wrong order is a common source of errors.
- Check boundary-sized inputs before relying on the general iteration.

## Notion Notes

Detailed explanation, code walkthrough, dry run and diagrams:

Notion page: TODO
