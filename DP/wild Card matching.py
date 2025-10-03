"""
Problem Description:
--------------------
LeetCode 44. Wildcard Matching
Link: https://leetcode.com/problems/wildcard-matching/

Given an input string (s) and a pattern (p), implement wildcard pattern matching with support for '?' and '*'.
'?' Matches any single character.
'*' Matches any sequence of characters (including the empty sequence).
The matching should cover the entire input string (not partial).

Example:
--------
Input: s = "adceb", p = "*a*b"
Output: true
Explanation: The first '*' matches the empty sequence, while the second '*' matches the substring "dce".

"""

#!IDEA
"""
This problem can be solved using Dynamic Programming with memoization (top-down approach).
We define a recursive function `solve(i, j)` that returns true if the first `i` characters of string `s` match the first `j` characters of pattern `p`.

The state of our recursion is `(i, j)`, representing `s[0...i]` and `p[0...j]`. We use 0-based indexing from the end of the strings for convenience, so `solve(i, j)` checks if `s[:i+1]` matches `p[:j+1]`.

The recursive logic is as follows:

Base Cases:
1. If both `i` and `j` are less than 0, it means we have successfully matched both the string and the pattern completely. Return `True`.
2. If `j < 0` (pattern is exhausted) but `i >= 0` (string is not), there's a mismatch. Return `False`.
3. If `i < 0` (string is exhausted) but `j >= 0` (pattern is not), we can only have a match if the remaining part of the pattern consists only of '*' characters. We check for this and return accordingly.

Recursive Steps:
1. If `p[j]` is '?' or `p[j] == s[i]`:
   The characters match. We can ignore these last characters and check the rest of the 
   strings. Recurse with `solve(i - 1, j - 1)`.

2. If `p[j]` is '*':
   The '*' can match in two ways:
   a) It matches an empty sequence. In this case, we ignore the '*' in the pattern and see 
   if the rest of the pattern `p[0...j-1]`
     matches the current string `s[0...i]`. This corresponds to `solve(i, j - 1)`.
   b) It matches one or more characters in the string `s`. In this case, we use the '*' to match `s[i]` and see if the same '*' can match more characters in the string. This corresponds to `solve(i - 1, j)`.
   If either of these possibilities returns true, then we have a match. So, the result is `solve(i - 1, j) or solve(i, j - 1)`.

3. If `p[j]` is a normal character and `p[j] != s[i]`:
   There is a mismatch. Return `False`.

To avoid recomputing results for the same `(i, j)` pairs, we use memoization, which is conveniently handled by `@lru_cache`.
"""

from functools import lru_cache

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        n, m = len(s), len(p)

        @lru_cache(None) # Memoization
        def solve(i: int, j: int) -> bool:
            # Base case 1: Both string and pattern are exhausted
            if i < 0 and j < 0:
                return True
            # Base case 2: Pattern is exhausted, but string is not
            if j < 0 and i >= 0:
                return False
            # Base case 3: String is exhausted, but pattern is not
            if i < 0 and j >= 0:
                # Remaining pattern must be all '*'
                for k in range(j + 1):
                    if p[k] != "*":
                        return False
                return True

            # Case 1: Characters match or pattern has '?'
            if p[j] == s[i] or p[j] == '?':
                return solve(i - 1, j - 1)

            # Case 2: Pattern has '*'
            if p[j] == "*":
                # '*' matches one char in s OR '*' matches empty sequence
                return solve(i - 1, j) or solve(i, j - 1) 

            # Case 3: Characters do not match
            return False

        return solve(n - 1, m - 1)

# --- Testing System ---
def test_solution(func, test_cases):
    for idx, (input_val, expected) in enumerate(test_cases, 1):
        s, p = input_val
        output = func(s, p)
        if output == expected:
            print(f"Test case {idx}: ✅ Passed")
        else:
            print(f"Test case {idx}: ❌ Failed")
            print(f"  Input: s='{s}', p='{p}'")
            print(f"  Output: {output}")
            print(f"  Expected: {expected}")

# --- Example Test Cases ---
if __name__ == "__main__":
    sol = Solution()
    test_cases = [
        (("aa", "a"), False),
        (("aa", "*"), True),
        (("cb", "?a"), False),
        (("adceb", "*a*b"), True),
        (("acdcb", "a*c?b"), False),
        (("", "*"), True),
        (("mississippi", "m??*ss*?i*pi"), False),
    ]
    
    test_solution(sol.isMatch, test_cases)

"""
Dry Run Example:
---------------
Input: s = "adceb", p = "*a*b"
Initial call: solve(i=4, j=3)

`solve(i, j)` checks if s[:i+1] matches p[:j+1]

1. solve(4, 3)  // s[4]='b', p[3]='b'
   - Characters match.
   - Returns solve(3, 2)

2. solve(3, 2)  // s[3]='e', p[2]='*'
   - p[2] is '*'. It can match 'e' or be empty.
   - Returns solve(2, 2) [match 'e'] OR solve(3, 1) [empty]

3. solve(3, 1)  // s[3]='e', p[1]='a'
   - Mismatch. Returns False.

4. solve(2, 2)  // s[2]='c', p[2]='*'
   - p[2] is '*'. It can match 'c' or be empty.
   - Returns solve(1, 2) [match 'c'] OR solve(2, 1) [empty]

5. solve(2, 1)  // s[2]='c', p[1]='a'
   - Mismatch. Returns False.

6. solve(1, 2)  // s[1]='d', p[2]='*'
   - p[2] is '*'. It can match 'd' or be empty.
   - Returns solve(0, 2) [match 'd'] OR solve(1, 1) [empty]

7. solve(1, 1)  // s[1]='d', p[1]='a'
   - Mismatch. Returns False.

8. solve(0, 2)  // s[0]='a', p[2]='*'
   - p[2] is '*'. It can match 'a' or be empty.
   - Returns solve(-1, 2) [match 'a'] OR solve(0, 1) [empty]

9. solve(0, 1)  // s[0]='a', p[1]='a'
   - Characters match.
   - Returns solve(-1, 0)

10. solve(-1, 0) // s is empty, p has '*' left
    - Base case 3: i < 0. Checks if remaining pattern p[0...0] is all '*'.
    - p[0] is '*', so it returns True.

Since solve(-1, 0) is True, the chain of ORs becomes True all the way up:
solve(0, 1) -> True
solve(0, 2) -> True
solve(1, 2) -> True
solve(2, 2) -> True
solve(3, 2) -> True
solve(4, 3) -> True

Final Answer: True
"""
