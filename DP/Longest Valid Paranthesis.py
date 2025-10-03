"""
Problem Description:
--------------------
[problem:] LeetCode 32. Longest Valid Parentheses
[link:] https://leetcode.com/problems/longest-valid-parentheses/
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
This problem can be solved using several approaches, including Dynamic Programming and a Stack.

--- Solution 1: Dynamic Programming ---
#*State*:
    - `dp[i]`: The length of the longest valid parentheses substring that *ends* at index `i`.

#*Core Logic*:
    - We iterate through the string `s` and populate the `dp` array.
    - If `s[i]` is '(': A valid substring cannot end with '(', so `dp[i]` is 0.
    - If `s[i]` is ')': We look at the previous character `s[i-1]`.
        1.  **Case `s[i-1] == '('` (e.g., "...()")**:
            We found a simple "()" pair. The length is 2 plus the length of any valid substring ending at `i-2`.
            `dp[i] = dp[i-2] + 2` (if `i-2` is a valid index).
        2.  **Case `s[i-1] == ')'` (e.g., "...))")**:
            If the substring ending at `i-1` is valid (length `dp[i-1]`), we look for a matching '(' for the current ')' at `s[i]`. This matching '(' would be at `i - dp[i-1] - 1`.
            If `s[i - dp[i-1] - 1]` is indeed '(', we have extended a valid substring.
            The new length is `dp[i-1]` (the inner part) + `2` (for the enclosing pair) + `dp[i - dp[i-1] - 2]` (for any valid part before the new one).

#*Result*:
    - The final answer is the maximum value found in the `dp` array.

#*Complexity*:
    - Time: O(n) because we iterate through the string once.
    - Space: O(n) for the `dp` array.

--- Solution 2: Stack-based Approach ---
#*State*:
    - A stack that stores indices of characters. We initialize it with `-1` to act as a sentinel value, providing a base for length calculation.

#*Core Logic*:
    - Iterate through the string with index `i` and character `ch`.
    - If `ch` is '(': Push its index `i` onto the stack.
    - If `ch` is ')':
        1. Pop an element from the stack. This is the matching '('.
        2. If the stack is now empty, it means the current ')' doesn't have a matching '('. We push the current index `i` onto the stack to serve as a new base for future valid substrings.
        3. If the stack is not empty, a valid substring has just ended at `i`. Its length is `i - stack[-1]` (current index minus the index of the character just before the start of this valid substring). We update our max length.

#* Result:
    - The maximum length calculated during the iteration.

#* Complexity:
    - Time: O(n) as we iterate through the string once.
    - Space: O(n) for the stack in the worst case (e.g., "(((((").
"""

class Solution:
    # Approach 1: Dynamic Programming
    def longestValidParentheses(self, s: str) -> int:
        if not s:
            return 0
            
        n = len(s)
        dp = [0] * n
        max_len = 0
        
        for i in range(1, n):
            if s[i] == ')':
                if s[i - 1] == '(':
                    # Case: ...()
                    dp[i] = (dp[i - 2] if i >= 2 else 0) + 2
                elif i - dp[i - 1] - 1 >= 0 and s[i - dp[i - 1] - 1] == '(':
                    # Case: ...))
                    dp[i] = dp[i - 1] + 2
                    # Add length of the valid substring before the new one
                    if i - dp[i - 1] - 2 >= 0:
                        dp[i] += dp[i - dp[i - 1] - 2]
            
            max_len = max(max_len, dp[i])

        return max_len
    
    # Approach 2: Stack
    def longestValidParentheses_stack(self, s: str) -> int:
        stack = [-1]  
        max_len = 0

        for i, ch in enumerate(s):
            if ch == "(":
                stack.append(i)
            else:
                stack.pop()
                if not stack:
                    stack.append(i)
                else:
                    max_len = max(max_len, i - stack[-1])

        return max_len

# --- Testing System ---
def test_solution(func, test_cases):
    for idx, (input_val, expected) in enumerate(test_cases, 1):
        output = func(input_val) # type: ignore
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
    print("--- Testing DP Solution ---")
    test_solution(sol.longestValidParentheses, test_cases)
    print("\n--- Testing Stack Solution ---")
    test_solution(sol.longestValidParentheses_stack, test_cases)

"""
Dry Run Example (DP):
---------------
Input: s = "(()())"
n = 6, dp = [0, 0, 0, 0, 0, 0], max_len = 0

i=0, s[0]='(': skip
i=1, s[1]='(': skip
i=2, s[2]=')', s[1]='(': Case "...()". dp[2] = dp[0] + 2 = 2. max_len=2.
    dp=[0,0,2,0,0,0]
i=3, s[3]='(': skip
i=4, s[4]=')', s[3]='(': Case "...()". dp[4] = dp[2] + 2 = 2 + 2 = 4. max_len=4.
    dp=[0,0,2,0,4,0]
i=5, s[5]=')', s[4]=')': Case "...))".
    - prev_len = dp[4] = 4.
    - Check for matching '(': s[i - prev_len - 1] = s[5 - 4 - 1] = s[0] = '('. Match!
    - dp[5] = dp[4] + 2 + dp[i - prev_len - 2] = dp[4] + 2 + dp[-1] (0) = 4 + 2 + 0 = 6.
    - max_len=6.
    dp=[0,0,2,0,4,6]

✅ Final Answer: 6

Dry Run Example (Stack):
---------------
Input: s = ")()())"
stack = [-1], max_len = 0

i=0, ch=')':
    - pop from stack. stack becomes [].
    - stack is empty, push i=0. stack=[0].

i=1, ch='(':
    - push i=1. stack=[0, 1].

i=2, ch=')':
    - pop from stack. stack becomes [0].
    - stack not empty. max_len = max(0, i - stack[-1]) = max(0, 2 - 0) = 2.

i=3, ch='(':
    - push i=3. stack=[0, 3].

i=4, ch=')':
    - pop from stack. stack becomes [0].
    - stack not empty. max_len = max(2, i - stack[-1]) = max(2, 4 - 0) = 4.

i=5, ch=')':
    - pop from stack. stack becomes [].
    - stack is empty, push i=5. stack=[5].

✅ Final Answer: 4
"""