"""
Problem Description:
--------------------
LeetCode 32. Longest Valid Parentheses
Link: https://leetcode.com/problems/longest-valid-parentheses/

Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed) parentheses substring.

Example:
--------
Input: s = "(()"
Output: 2
Explanation: The longest valid parentheses substring is "()".

Input: s = ")()())"
Output: 4
Explanation: The longest valid parentheses substring is "()()".

"""

#!IDEA
"""
This problem can be solved efficiently using Dynamic Programming.

Let `dp[i]` be the length of the longest valid parentheses substring ending at index `i`.
We initialize a `dp` array of the same size as the input string `s` with all zeros.
The `dp` array is populated by iterating through the string from left to right.

The logic for updating `dp[i]` is as follows:

1. If `s[i]` is '(':
   A valid substring cannot end with an opening bracket, so `dp[i]` remains 0.

2. If `s[i]` is ')':
   We have two sub-cases to consider based on the character `s[i-1]`.

   a) If `s[i-1]` is '(':
      This means we have found a pair "()". The length of this pair is 2.
      We can extend this by adding the length of the longest valid substring ending at `i-2`.
      So, `dp[i] = (dp[i-2] if i >= 2 else 0) + 2`.

   b) If `s[i-1]` is ')':
      This indicates a structure like `...))`. The substring ending at `i-1` is a valid one with length `dp[i-1]`.
      We need to check if there is a matching opening bracket for the current `s[i]`.
      The potential matching '(' would be at index `i - dp[i-1] - 1`.
      If this index is valid and `s[i - dp[i-1] - 1] == '('`, we have formed a larger valid substring.
      The length of this new substring is:
      - The length of the inner valid substring (`dp[i-1]`).
      - Plus 2 for the enclosing `()` pair.
      - Plus the length of any valid substring that appeared just before this new one (at `dp[i - dp[i-1] - 2]`).
      So, `dp[i] = dp[i-1] + 2 + (dp[i - dp[i-1] - 2] if (i - dp[i-1] - 2 >= 0) else 0)`.

The maximum value in the `dp` array will be the length of the longest valid parentheses substring in the entire string.
"""

class Solution:
    def longestValidParentheses(self, s: str) -> int:
        if not s:
            return 0
            
        n = len(s)
        dp = [0] * n
        ans = 0
        
        for i in range(1, n):
            if s[i] == ')':
                if s[i - 1] == '(':
                    # Case 1: ...()
                    dp[i] = (dp[i - 2] if i >= 2 else 0) + 2
                elif i - dp[i - 1] - 1 >= 0 and s[i - dp[i - 1] - 1] == '(':
                    # Case 2: ...))
                    dp[i] = dp[i - 1] + 2
                    # Add length of the valid substring before the new one
                    if i - dp[i - 1] - 2 >= 0:
                        dp[i] += dp[i - dp[i - 1] - 2]
            
            ans = max(ans, dp[i])

        return ans
    
    def longestValidParentheses1(self, s: str) -> int:
        stack = [-1]  
        ans = 0

        for i, ch in enumerate(s):
            if ch == "(":
                stack.append(i)
            else:
                stack.pop()
                if not stack:
                    stack.append(i)
                else:
                    ans = max(ans, i - stack[-1])

        return ans

# --- Testing System ---
def test_solution(func, test_cases):
    for idx, (input_val, expected) in enumerate(test_cases, 1):
        output = func(input_val)
        if output == expected:
            print(f"Test case {idx}: ✅ Passed")
        else:
            print(f"Test case {idx}: ❌ Failed")
            print(f"  Input: '{input_val}'")
            print(f"  Output: {output}")
            print(f"  Expected: {expected}")

# --- Example Test Cases ---
if __name__ == "__main__":
    sol = Solution()
    test_cases = [
        ("(()", 2),
        (")()())", 4),
        ("", 0),
        ("()(()", 2),
        ("()(())", 6),
        ("((()))", 6),
    ]
    
    test_solution(sol.longestValidParentheses, test_cases)

"""
Dry Run Example:
---------------
Input: s = "()(())"
n = 6, dp = [0, 0, 0, 0, 0, 0], ans = 0

i=1, s[1]=')', s[0]='('. Case 1. dp[1] = dp-1 + 2 = 2. ans=2. dp=[0,2,0,0,0,0]
i=2, s[2]='('. dp[2]=0. ans=2. dp=[0,2,0,0,0,0]
i=3, s[3]=')', s[2]='('. Case 1. dp[3] = dp[1] + 2 = 2 + 2 = 4. ans=4. dp=[0,2,0,4,0,0]
i=4, s[4]=')', s[3]=')'. Case 2. prev_len=dp[3]=4. Check s[4-4-1]=s[-1] -> invalid. dp[4]=0. ans=4. dp=[0,2,0,4,0,0]
i=5, s[5]=')', s[4]=')'. Case 2. prev_len=dp[4]=0. Check s[5-0-1]=s[4]=')' -> mismatch. dp[5]=0.
Wait, my dry run is wrong. Let's re-trace.

Input: s = "()(())"
n = 6, dp = [0, 0, 0, 0, 0, 0], ans = 0

i=0, s[0]='(': skip
i=1, s[1]=')', s[0]='(': Case 1. dp[1] = (dp[-1] -> 0) + 2 = 2. ans=max(0,2)=2. dp=[0,2,0,0,0,0]
i=2, s[2]='(': skip
i=3, s[3]=')', s[2]='(': Case 1. dp[3] = dp[1] + 2 = 2 + 2 = 4. ans=max(2,4)=4. dp=[0,2,0,4,0,0]
i=4, s[4]='(': skip
i=5, s[5]=')', s[4]='(': Case 1. dp[5] = dp[3] + 2 = 4 + 2 = 6. ans=max(4,6)=6. dp=[0,2,0,4,0,6]

Final dp: [0, 2, 0, 4, 0, 6]
Final ans: 6

Let's try s = "(()())"
n = 6, dp = [0, 0, 0, 0, 0, 0], ans = 0

i=1, s[1]='(': skip
i=2, s[2]=')', s[1]='(': Case 1. dp[2] = dp[0] + 2 = 0 + 2 = 2. ans=2. dp=[0,0,2,0,0,0]
i=3, s[3]='(': skip
i=4, s[4]=')', s[3]='(': Case 1. dp[4] = dp[2] + 2 = 2 + 2 = 4. ans=4. dp=[0,0,2,0,4,0]
i=5, s[5]=')', s[4]=')': Case 2. prev_len=dp[4]=4. Check s[5-4-1]=s[0]='('. Match!
  dp[5] = dp[4] + 2 + dp[5-4-2]=dp-1 = 4 + 2 + 0 = 6. ans=6. dp=[0,0,2,0,4,6]

Final ans: 6
"""