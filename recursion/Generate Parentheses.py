"""
Given n pairs of parentheses, write a function to generate all combinations
of well-formed parentheses.

Example 1:

Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]

"""

#!IDEA
"""
use recursion
track of open and close braces
if close==open got your ans save it

"""


class Solution:
    def generateParenthesis(self, n: int):
        res = []
        
        def backtrack(s, open_count, close_count):
            if len(s) == 2 * n:
                res.append(s)
                return
            
            if open_count < n:
                backtrack(s + '(', open_count + 1, close_count)
            
            if close_count < open_count:
                backtrack(s + ')', open_count, close_count + 1)
        
        backtrack("", 0, 0)
        return res


# --- Testing System ---
def test_solution(func, test_cases):
    for idx, (input_val, expected) in enumerate(test_cases, 1):
        output = func(input_val)
        # Sort both lists because order may vary
        if sorted(output) == sorted(expected):
            print(f"Test case {idx}: ✅ Passed")
        else:
            print(f"Test case {idx}: ❌ Failed")
            print(f"  Input: {input_val}")
            print(f"  Output: {output}")
            print(f"  Expected: {expected}")


# --- Example Test Cases ---
if __name__ == "__main__":
    sol = Solution()
    test_cases = [
        (3, ["((()))","(()())","(())()","()(())","()()()"]),
        (1, ["()"]),
        (2, ["(())","()()"]),
    ]
    
    test_solution(sol.generateParenthesis, test_cases)

