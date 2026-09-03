# 893 — Groups of Special-Equivalent Strings

**Difficulty:** Medium

**LeetCode:** https://leetcode.com/problems/groups-of-special-equivalent-strings/

## Topics

Official LeetCode Topics:
- Array
- Hash Table
- String
- Sorting

Study Patterns:
- Canonical Representation
- Hashing

## Intuition

A special-equivalent operation swaps characters only at indices with the same
parity. Therefore, the characters at even indices can be rearranged among
themselves, and the characters at odd indices can be rearranged among
themselves, but characters cannot move between those two sets.

Two words belong to the same group exactly when their sorted even-indexed
characters and sorted odd-indexed characters are identical.

## Approach

1. Extract and sort the characters at the even indices of each word.
2. Extract and sort the characters at the odd indices.
3. Combine both sorted sequences into a canonical signature.
4. Store every signature in a set and return the number of unique signatures.

## Complexity

Let `n` be the number of words and `k` be the length of each word.

- Time: O(n × k log k)
- Space: O(n × k)

## Solution

[View Python solution](./solution.py)

## Interview Notes

- The key invariant is that character-index parity never changes.
- A canonical signature turns the equivalence-group problem into set counting.
- Keep the even and odd character collections separate when constructing the
  signature.

## Notion Notes

Detailed explanation, code walkthrough, dry run and diagrams:

Notion page: [https://app.notion.com/p/3d050eec34db81178179fa3e01895cb8?pvs=204](https://app.notion.com/p/3d050eec34db81178179fa3e01895cb8?pvs=204)
