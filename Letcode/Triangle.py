"""
Problem Description:
--------------------
LeetCode 120. Triangle
Link: https://leetcode.com/problems/triangle/

Given a triangle array, find the minimum path sum from top to bottom.
For each step, you may move to an adjacent number of the row below. More formally, if you are on index i on the current row, you may move to either index i or index i + 1 on the next row.

Example:
--------
Input: triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
Output: 11
Explanation: The minimum path sum from top to bottom is 2 + 3 + 5 + 1 = 11.
   2
  3 4
 6 5 7
4 1 8 3

"""

#!IDEA
"""
This problem can be solved efficiently using bottom-up dynamic programming. The key idea is to modify the triangle in-place to store the minimum path sums starting from each cell.

1.  **Approach**: We start from the second-to-last row and move upwards to the top.
2.  **Iteration**: For each element `triangle[i][j]`, we calculate the minimum path sum starting from that element. This sum is the element's own value plus the minimum of the two adjacent elements in the row directly below it (`triangle[i+1][j]` and `triangle[i+1][j+1]`).
3.  **Update**: We update `triangle[i][j]` with this new calculated sum.
4.  **Result**: By the time we reach the top of the triangle, the element `triangle[0][0]` will hold the overall minimum path sum from the top to the bottom.

This approach is space-efficient as it modifies the input array, using O(1) extra space. The time complexity is O(N^2), where N is the number of rows, as we visit each element once.
"""

from typing import List

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        # Iterate from the second-to-last row up to the top row
        for i in range(n-2,-1,-1):
            for j in range(len(triangle[i])):
                # Update the current element with the minimum path sum starting from it
                triangle[i][j] += min(triangle[i+1][j],triangle[i+1][j+1])

        # The top element now contains the overall minimum path sum
        return triangle[0][0]


# --- Testing System ---
def test_solution(func, test_cases):
    for idx, (input_val, expected) in enumerate(test_cases, 1):
        # The function modifies the input list, so we pass a copy
        input_copy = [row[:] for row in input_val]
        output = func(input_copy)
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
        ([[2],[3,4],[6,5,7],[4,1,8,3]], 11),
        ([[-10]], -10),
        ([[-1],[2,3],[1,-1,-3]], -1),
    ]
    
    test_solution(sol.minimumTotal, test_cases)


"""
Dry Run Example:
---------------
Input: triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]

🎯 Start from second-to-last row (i=2)

└── i = 2 (row [6, 5, 7]):
    ├── j=0: triangle[2][0] = 6 + min(triangle[3][0], triangle[3][1]) = 6 + min(4, 1) = 7
    ├── j=1: triangle[2][1] = 5 + min(triangle[3][1], triangle[3][2]) = 5 + min(1, 8) = 6
    └── j=2: triangle[2][2] = 7 + min(triangle[3][2], triangle[3][3]) = 7 + min(8, 3) = 10
    Triangle is now: [[2], [3,4], [7,6,10], [4,1,8,3]]

└── i = 1 (row [3, 4]):
    ├── j=0: triangle[1][0] = 3 + min(triangle[2][0], triangle[2][1]) = 3 + min(7, 6) = 9
    └── j=1: triangle[1][1] = 4 + min(triangle[2][1], triangle[2][2]) = 4 + min(6, 10) = 10
    Triangle is now: [[2], [9,10], [7,6,10], [4,1,8,3]]

└── i = 0 (row [2]):
    └── j=0: triangle[0][0] = 2 + min(triangle[1][0], triangle[1][1]) = 2 + min(9, 10) = 11
    Triangle is now: [[11], [9,10], [7,6,10], [4,1,8,3]]

✅ Final Answer: triangle[0][0] which is 11.
"""