# Sort a Stack

**Difficulty:** Not reliably specified

**Platform:** GeeksforGeeks

**Problem:** https://www.geeksforgeeks.org/problems/sort-a-stack/1

## Topics

Study Topics:
- Stack
- Recursion

Study Patterns:
- Recursion and Partitioning
- Stack and Queue Techniques

## Intuition

The unresolved items in sort a stack must be handled in a specific last-in or first-in order. The stack or queue stores exactly those pending items until they can be resolved.

## Approach

1. Initialize the stack or queue holding unresolved state.
2. Process each item, removing entries that the current item completes and adding those still pending.
3. Build or return the result from the final data-structure state.

## Complexity

- Time: O(n²)
- Space: O(n) recursion stack

## Solution

[View Python solution](./solution.py)

## Interview Notes

- Recognize this problem when its constraints match the Recursion and Partitioning pattern.
- Keep the core invariant explicit; updating state in the wrong order is a common source of errors.
- Check boundary-sized inputs before relying on the general iteration.

## Notion Notes

Detailed explanation, code walkthrough, dry run and diagrams:

Notion page: TODO
