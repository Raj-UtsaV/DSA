"""
Problem Description:
--------------------
LeetCode 6. Zigzag Conversion
Link: https://leetcode.com/problems/zigzag-conversion/

The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this:
P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows.

Example:
--------
Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"

"""

#!IDEA
"""
The problem can be solved by simulating the zigzag pattern. We can create a list of lists (or strings) to represent the rows of the zigzag pattern.

1.  **Initialization**: Create a list of `numRows` empty lists, where each inner list will store the characters for that row.
2.  **Edge Cases**: If `numRows` is 1 or greater than the length of the string, the zigzag pattern doesn't change the string, so we can return the original string.
3.  **Traversal**: Iterate through each character of the input string `s`.
    - Keep track of the current row index (`idx`) and the direction of movement (`d`). The direction is `1` for moving down and `-1` for moving up.
    - Append the current character to the list at `mat[idx]`.
4.  **Direction Change**: The direction of traversal flips when we reach the top row (index 0) or the bottom row (index `numRows - 1`).
    - If `idx` is 0, set direction `d` to 1 (down).
    - If `idx` is `numRows - 1`, set direction `d` to -1 (up).
5.  **Update Index**: After appending the character, update the row index by adding the direction: `idx += d`.
6.  **Final String**: After iterating through all characters, join the characters in each row's list, and then join all the resulting row strings to get the final answer.
"""

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s
        
        # `idx` is the current row, `d` is the direction (1 for down, -1 for up)
        idx,d = 0,1
        # A list of lists to hold characters for each row
        mat = [[]for _ in range(numRows)]

        for c in s:
            mat[idx].append(c)
            # Change direction if we are at the top or bottom row
            if idx == 0:
                d = 1
            elif idx == numRows-1:
                d = -1
            idx += d

        # Join characters in each row
        for i in range(numRows):
            mat[i] = ''.join(mat[i])
        
        # Join all rows to form the final string
        return ''.join(mat)

# --- Testing System ---
def test_solution(func, test_cases):
    for idx, (input_val, expected) in enumerate(test_cases, 1):
        # The function expects two arguments, so we unpack the input tuple
        output = func(*input_val)
        if output == expected:
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
        (("PAYPALISHIRING", 3), "PAHNAPLSIIGYIR"),
        (("PAYPALISHIRING", 4), "PINALSIGYAHRPI"),
        (("A", 1), "A"),
        (("AB", 1), "AB"),
    ]
    
    test_solution(sol.convert, test_cases)

"""
Dry Run Example:
---------------
Input: s = "PAYPALISHIRING", numRows = 3

mat = [[], [], []], idx = 0, d = 1

P -> mat[0].append('P') -> [['P'], [], []], idx=1
A -> mat[1].append('A') -> [['P'], ['A'], []], idx=2
Y -> mat[2].append('Y') -> [['P'], ['A'], ['Y']], idx=1 (d becomes -1)
P -> mat[1].append('P') -> [['P'], ['A', 'P'], ['Y']], idx=0
A -> mat[0].append('A') -> [['P', 'A'], ['A', 'P'], ['Y']], idx=1 (d becomes 1)
L -> mat[1].append('L') -> [['P', 'A'], ['A', 'P', 'L'], ['Y']], idx=2
... and so on.

After loop, mat will be:
mat[0] = ['P', 'A', 'H', 'N']
mat[1] = ['A', 'P', 'L', 'S', 'I', 'I', 'G']
mat[2] = ['Y', 'I', 'R']

Join each row:
row0 = "PAHN"
row1 = "APLSIIG"
row2 = "YIR"

Join all rows: "PAHN" + "APLSIIG" + "YIR" -> "PAHNAPLSIIGYIR"
"""