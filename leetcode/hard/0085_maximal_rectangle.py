"""Canonical solution metadata.

Problem Number: 85
Problem Title: Maximal Rectangle
Platform: LeetCode
Difficulty: Hard
Official Platform Topics: Array, Dynamic Programming, Stack, Matrix, Monotonic Stack
Study Tags: Histogram reduction
Canonical URL: https://leetcode.com/problems/maximal-rectangle/
"""

"""
Problem Description:
--------------------
LeetCode 85. Maximal Rectangle
Link: https://leetcode.com/problems/maximal-rectangle/

Given a `rows x cols` binary `matrix` filled with 0's and 1's, find the largest rectangle containing only 1's and return its area.

Example:
--------
Input: matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
Output: 6
Explanation: The maximal rectangle is shown in the example on LeetCode.

"""

#!IDEA
"""
The problem of finding the maximal rectangle of 1s in a 2D matrix can be cleverly reduced to a series of "Largest Rectangle in Histogram" problems.

1.  **Histogram Representation**:
    We can think of each row of the matrix as the base of a histogram. The height of each bar in the histogram at column `j` is the number of consecutive 1s directly above the current cell `(i, j)`, including the cell itself.

2.  **Iterate Through Rows**:
    - We iterate through the matrix row by row, from top to bottom.
    - We maintain a `heights` array (or `v` in the code) of the same width as the matrix. This array will store the heights of the histogram for the current row being processed.

3.  **Build Heights**:
    - For each cell `(i, j)`:
        - If `matrix[i][j]` is '1', the height at that position increases by 1: `heights[j] = heights[j] + 1`.
        - If `matrix[i][j]` is '0', the streak of 1s is broken, so the height at that position resets to 0: `heights[j] = 0`.

4.  **Calculate Max Area for Each Row**:
    - After updating the `heights` array for a given row `i`, we have a histogram.
    - We then calculate the largest rectangle in this histogram using the well-known monotonic stack algorithm (implemented in the `max_area` helper function).
    - This algorithm finds, for each bar, the nearest smaller bars to its left and right, which determines the width of the largest rectangle that can be formed with that bar as the height.

5.  **Track Overall Maximum**:
    - We keep a global maximum area variable (`ans` in the code) and update it with the result from each row's histogram calculation.

6.  **Return Result**:
    - After iterating through all the rows, the global maximum area variable will hold the area of the maximal rectangle in the entire matrix.

The time complexity is O(rows * cols) because we iterate through each cell once to build the histogram, and the histogram area calculation for each row is O(cols). The space complexity is O(cols) to store the heights array.
"""

from typing import List

class Solution:
    def max_area(self, heights: List[int]) -> int:
        """
        Calculates the largest rectangle area in a histogram using a monotonic stack.
        This is a helper function based on LeetCode 84.
        """
        st = []
        max_area_val = 0
        n = len(heights)

        for i in range(n):
            while st and heights[st[-1]] >= heights[i]:
                element = st.pop()
                pse = st[-1] if st else -1
                nse = i
                max_area_val = max(max_area_val, heights[element] * (nse - pse - 1))
            st.append(i)

        # Process remaining elements in the stack
        while st:
            element = st.pop()
            pse = st[-1] if st else -1
            nse = n
            max_area_val = max(max_area_val, heights[element] * (nse - pse - 1))

        return max_area_val

    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix or not matrix[0]:
            return 0

        ans = 0
        n, m = len(matrix), len(matrix[0])
        heights = [0] * m

        # Iterate through each row of the matrix
        for i in range(n):
            # Update the heights of the histogram for the current row
            for j in range(m):
                if matrix[i][j] == '1':
                    heights[j] += 1
                else:
                    heights[j] = 0

            # Calculate the max area for the histogram formed by the current row
            ans = max(ans, self.max_area(heights))

        return ans

# --- Testing System ---
def test_solution(func, test_cases):
    for idx, (input_val, expected) in enumerate(test_cases, 1):
        output = func(input_val)
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
        ([["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]], 6),
        ([["0"]], 0),
        ([["1"]], 1),
        ([["0","0"]], 0),
        ([["1","1","1"],["1","1","1"],["1","1","1"]], 9)
    ]

    test_solution(sol.maximalRectangle, test_cases)

"""
Dry Run Example:
---------------
Input: matrix = [["1","0","1"], ["1","1","1"], ["1","1","1"]]

heights = [0, 0, 0], ans = 0

└── Row 0 (i=0):
    - heights becomes [1, 0, 1]
    - max_area([1, 0, 1]) = 1
    - ans = max(0, 1) = 1

└── Row 1 (i=1):
    - heights becomes [1+1, 0+1, 1+1] -> [2, 1, 2]
    - max_area([2, 1, 2]) = 3 (from the middle bar of height 1, width 3)
    - ans = max(1, 3) = 3

└── Row 2 (i=2):
    - heights becomes [2+1, 1+1, 2+1] -> [3, 2, 3]
    - max_area([3, 2, 3]) = 6 (from the middle bar of height 2, width 3)
    - ans = max(3, 6) = 6

✅ Final Answer: 6
"""
