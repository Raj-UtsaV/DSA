# Number of Graphs with N Vertices

**Difficulty:** Not reliably specified

**Platform:** GeeksforGeeks

**Problem:** https://www.geeksforgeeks.org/problems/number-of-graphs-with-n-vertices/1

## Topics

Study Topics:
- Combinatorics
- Modular Exponentiation

Study Patterns:
- Combinatorics
- Modular Exponentiation

## Intuition

The implementation solves number of graphs with n vertices by scanning the relevant input while maintaining the smallest state needed for the answer. Each item is incorporated once in the order required by the Combinatorics technique.

## Approach

1. Initialize the state required by the Combinatorics invariant.
2. Process each relevant input item and update the candidate result.
3. Return the accumulated or validated result after the scan completes.

## Complexity

- Time: O(log n)
- Space: O(log n) recursion stack

## Solution

[View Python solution](./solution.py)

## Interview Notes

- Recognize this problem when its constraints match the Combinatorics pattern.
- Keep the core invariant explicit; updating state in the wrong order is a common source of errors.
- Check boundary-sized inputs before relying on the general iteration.

## Notion Notes

Detailed explanation, code walkthrough, dry run and diagrams:

Notion page: TODO
