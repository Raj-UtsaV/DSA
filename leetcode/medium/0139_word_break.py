"""Canonical solution metadata.

Problem Number: 139
Problem Title: Word Break
Platform: LeetCode
Difficulty: Medium
Official Platform Topics: Array, Hash Table, String, Dynamic Programming, Trie, Memoization, Brute-Force Search
Study Tags: Top-down DP
Canonical URL: https://leetcode.com/problems/word-break/
"""

"""
LeetCode 139. Word Break
Link: https://leetcode.com/problems/word-break/

Given a string s and a dictionary of strings wordDict, return true 
if s can be segmented into a space-separated sequence of one or more dictionary words.

Note that the same word in the dictionary may be reused multiple times in the segmentation.

Example 1:
Input: s = "leetcode", wordDict = ["leet","code"]
Output: true

Example 2:
Input: s = "applepenapple", wordDict = ["apple","pen"]
Output: true

Example 3:
Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
Output: false
"""

#!IDEA
"""
We use recursion with memoization (top-down DP):
- Start from index `0`, try all possible substrings s[start:end].
- If substring is in wordDict, recursively check from `end`.
- If we reach the end of the string, return True.
- Use memo[start] to avoid recomputation.
- If no valid segmentation is found, return False.

Time Complexity: O(n^2) because we try all substrings (n choices for start, n choices for end).
Space Complexity: O(n) for recursion stack + memo.
"""

from typing import List

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordSet = set(wordDict)   # fast lookup
        memo = {}

        def backtrack(start: int) -> bool:
            if start == len(s):
                return True
            if start in memo:
                return memo[start]

            for end in range(start + 1, len(s) + 1):
                if s[start:end] in wordSet and backtrack(end):
                    memo[start] = True
                    return True

            memo[start] = False
            return False

        return backtrack(0)


# --- Testing System ---
def test_solution(func, test_cases):
    for idx, (s, wordDict, expected) in enumerate(test_cases, 1):
        output = func(s, wordDict)
        if output == expected:
            print(f"Test case {idx}: ✅ Passed")
        else:
            print(f"Test case {idx}: ❌ Failed")
            print(f"  Input: s={s}, wordDict={wordDict}")
            print(f"  Output: {output}")
            print(f"  Expected: {expected}")


# --- Example Test Cases ---
if __name__ == "__main__":
    sol = Solution()
    test_cases = [
        ("leetcode", ["leet","code"], True),
        ("applepenapple", ["apple","pen"], True),
        ("catsandog", ["cats","dog","sand","and","cat"], False),
    ]
    test_solution(sol.wordBreak, test_cases)


#! --- Dry Run Example ---
"""
Dry Run: s = "leetcode", wordDict = ["leet","code"]

1. backtrack(0):
   - try "l", "le", "lee" → not in dict
   - try "leet" → in dict → call backtrack(4)

2. backtrack(4):
   - try "c", "co", "cod" → not in dict
   - try "code" → in dict → call backtrack(8)

3. backtrack(8):
   - start == len(s), return True

=> backtrack(4) returns True
=> backtrack(0) returns True

Final Answer: True
"""
