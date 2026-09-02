# Job Sequencing Problem

**Difficulty:** Not reliably specified

**Platform:** GeeksforGeeks

**Problem:** https://www.geeksforgeeks.org/problems/job-sequencing-problem-1587115620/1

## Topics

Study Topics:
- Greedy Scheduling

Study Patterns:
- Greedy
- Interval Problems

## Intuition

A locally optimal choice for job sequencing problem leaves the greatest flexibility for the remaining input. Ordering the candidates makes that safe choice available at each step.

## Approach

1. Order candidates by the criterion used by the greedy invariant.
2. Accept a candidate when it is compatible with the choices already made.
3. Return the accumulated count, value, or selected arrangement.

## Complexity

- Time: O(n²) in the worst case
- Space: O(n)

## Solution

[View Python solution](./solution.py)

## Interview Notes

- Recognize this problem when its constraints match the Greedy pattern.
- Keep the core invariant explicit; updating state in the wrong order is a common source of errors.
- Check boundary-sized inputs before relying on the general iteration.

## Notion Notes

Detailed explanation, code walkthrough, dry run and diagrams:

Notion page: TODO
