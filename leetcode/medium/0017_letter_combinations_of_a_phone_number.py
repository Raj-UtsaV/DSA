"""Canonical solution metadata.

Problem Number: 17
Problem Title: Letter Combinations of a Phone Number
Platform: LeetCode
Difficulty: Medium
Official Platform Topics: Hash Table, String, Backtracking
Study Tags: Decision tree
Canonical URL: https://leetcode.com/problems/letter-combinations-of-a-phone-number/
"""

"""
Problem Description:
--------------------
LeetCode 17. Letter Combinations of a Phone Number
Link: https://leetcode.com/problems/letter-combinations-of-a-phone-number/

Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.

A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.

Example:
--------
Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

"""

#!IDEA
"""
We use backtracking to generate all combinations.
- Create a mapping from digits to their corresponding characters (`digit_to_char`).
- Define a recursive helper function `backtrack(index, current_combination)`.
- Base Case: If `index` reaches the length of `digits`, a complete combination is formed, so add it to `res`.
- Recursive Step: For the digit at `digits[index]`, iterate through its possible letters. For each letter, append it to `current_combination` and recursively call `backtrack` for the next `index`.
"""

from typing import List
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        res = []
        digit_to_char = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz',
        }

        def backtrack(index, current_combination):
            if index == len(digits):
                res.append(current_combination)
                return

            possible_letters = digit_to_char[digits[index]]
            for letter in possible_letters:
                backtrack(index + 1, current_combination + letter)

        backtrack(0, "")

        return res

# --- Testing System ---
def test_solution(func, test_cases):
    for idx, (input_val, expected) in enumerate(test_cases, 1):
        output = func(input_val)
        # Sort both lists because the order of combinations does not matter.
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
        ("23", ["ad","ae","af","bd","be","bf","cd","ce","cf"]),
        ("", []),
        ("2", ["a", "b", "c"]),
    ]
    test_solution(sol.letterCombinations, test_cases)

"""
Dry Run Example:
---------------
Input: digits = "23"

1. backtrack(0, ""):
   - index=0, digit='2', letters="abc"
   - For 'a': call backtrack(1, "a")
     - index=1, digit='3', letters="def"
     - For 'd': call backtrack(2, "ad") -> base case, res.append("ad")
     - For 'e': call backtrack(2, "ae") -> res.append("ae")
     - For 'f': call backtrack(2, "af") -> res.append("af")
   - For 'b': call backtrack(1, "b") -> generates "bd", "be", "bf"
   - For 'c': call backtrack(1, "c") -> generates "cd", "ce", "cf"

Final Answer: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]
"""
