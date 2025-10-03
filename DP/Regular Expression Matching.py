"""
Problem Description:
--------------------
LeetCode 10. Regular Expression Matching
Link: https://leetcode.com/problems/regular-expression-matching/

Given an input string (s) and a pattern (p), implement regular expression matching with support for '.' and '*'.
'.' Matches any single character.
'*' Matches zero or more of the preceding element.
The matching should cover the entire input string (not partial).

Example:
--------
Input: s = "aab", p = "c*a*b"
Output: true
Explanation: c can be repeated 0 times, a can be repeated 1 time. Therefore, it matches "aab".

"""

#!IDEA
"""
This problem is a classic dynamic programming challenge. We can solve it using a top-down DP approach with memoization.

Let's define a recursive function `solve(i, j)` which returns `True` if the substring `s[i:]` matches the sub-pattern `p[j:]`. We use 0-based indexing from the start of the strings.

The state of our recursion is `(i, j)`, representing the current positions in the string `s` and pattern `p`.

The recursive logic is as follows:

Base Case:
1. If we have exhausted the pattern (`j == len(p)`), the match is successful only if we have also exhausted the string (`i == len(s)`).

Recursive Steps:
We look at the current characters `s[i]` and `p[j]`.

1. Check for a '*' character:
   If the next character in the pattern is a `*` (i.e., `p[j+1] == '*'`), we have two choices for the `p[j]*` part:
   a) Zero-occurrence: The `*` matches zero instances of the preceding element `p[j]`. In this case, we can ignore `p[j]*` and see if the rest of the pattern `p[j+2:]` matches the current string `s[i:]`. This corresponds to `solve(i, j + 2)`.
   b) One-or-more occurrences: If the current character `s[i]` matches `p[j]` (or `p[j]` is '.'), the `*` can match one or more characters. We consume `s[i]` and stay at the same pattern position `j` to allow `*` to match more characters. This corresponds to `match and solve(i + 1, j)`.
   The result is `True` if either choice leads to a match.

2. Standard Match:
   If the next character is not a `*`, we must have a direct match between `s[i]` and `p[j]`.
   A match occurs if `s[i] == p[j]` or `p[j] == '.'`.
   If they match, we move to the next characters in both the string and the pattern: `solve(i + 1, j + 1)`.

3. Mismatch:
   If none of the above conditions are met, it's a mismatch, and we return `False`.

To optimize, we use memoization (e.g., `@lru_cache` or a dictionary) to store the results of `solve(i, j)` to avoid recomputing for the same state.
"""

from functools import lru_cache

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        @lru_cache(None)
        def solve(i: int, j: int) -> bool:
            # Base case: If pattern is exhausted, string must also be exhausted.
            if j == len(p):
                return i == len(s)

            # Check if current characters match
            first_match = i < len(s) and (p[j] == s[i] or p[j] == '.')

            # Case 1: The next character in pattern is '*'
            if j + 1 < len(p) and p[j+1] == '*':
                # Two choices for '*':
                # 1. Zero occurrences of p[j]: skip 'p[j]*' and move to p[j+2]
                # 2. One occurrence of p[j]: if first_match is true, move to next char in s
                return solve(i, j + 2) or (first_match and solve(i + 1, j))

            # Case 2: Standard match (no '*')
            if first_match:
                return solve(i + 1, j + 1)

            # No match found
            return False

        return solve(0, 0)

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
        (("aa", "a*"), True),
        (("ab", ".*"), True),
        (("aab", "c*a*b"), True),
        (("mississippi", "mis*is*p*."), False),
        (("", ".*"), True),
        (("ab", ".*c"), False),
    ]
    
    test_solution(sol.isMatch, test_cases)

"""
Dry Run Example:
---------------
Input: s = "aab", p = "c*a*b"
Initial call: solve(i=0, j=0)

`solve(i, j)` checks if s[i:] matches p[j:]

1. solve(0, 0)  // s="aab", p="c*a*b"
   - p[1] is '*'. Two choices for 'c*':
   - Choice 1 (zero 'c's): solve(0, 2)
   - Choice 2 (one 'c'): first_match is False (s[0]='a' != p[0]='c'). So this path is invalid.
   - Returns solve(0, 2)

2. solve(0, 2)  // s="aab", p="a*b"
   - p[3] is '*'. Two choices for 'a*':
   - Choice 1 (zero 'a's): solve(0, 4)
   - Choice 2 (one 'a'): first_match is True (s[0]='a' == p[2]='a'). Recurse with solve(1, 2).
   - Returns solve(0, 4) or solve(1, 2)

3. solve(0, 4)  // s="aab", p="b"
   - No '*' follows. first_match is False (s[0]='a' != p[4]='b'). Returns False.

4. solve(1, 2)  // s="ab", p="a*b"
   - p[3] is '*'. Two choices for 'a*':
   - Choice 1 (zero 'a's): solve(1, 4)
   - Choice 2 (one 'a'): first_match is True (s[1]='a' == p[2]='a'). Recurse with solve(2, 2).
   - Returns solve(1, 4) or solve(2, 2)

5. solve(1, 4)  // s="ab", p="b"
   - No '*' follows. first_match is False (s[1]='a' != p[4]='b'). Returns False.

6. solve(2, 2)  // s="b", p="a*b"
   - p[3] is '*'. Two choices for 'a*':
   - Choice 1 (zero 'a's): solve(2, 4)
   - Choice 2 (one 'a'): first_match is False (s[2]='b' != p[2]='a'). This path is invalid.
   - Returns solve(2, 4)

7. solve(2, 4)  // s="b", p="b"
   - No '*' follows. first_match is True (s[2]='b' == p[4]='b').
   - Returns solve(3, 5)

8. solve(3, 5)  // s="", p=""
   - Base case: j == len(p) (5==5). Check i == len(s) (3==3). It's True.
   - Returns True.

The True result propagates up the call stack:
solve(2, 4) -> True
solve(2, 2) -> True
solve(1, 2) -> True
solve(0, 2) -> True
solve(0, 0) -> True

✅ Final Answer: True
"""
