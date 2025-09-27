"""
Problem Description:
--------------------
LeetCode 812. Largest Triangle Area
Link: https://leetcode.com/problems/largest-triangle-area/

Given an array of points on the X-Y plane `points`, return the area of the largest triangle that can be formed by any three different points.

Example:
--------
Input: points = [[0,0],[0,1],[1,0],[0,2],[2,0]]
Output: 2.00000

"""

#!IDEA
"""
The problem asks for the area of the largest triangle that can be formed by any three points from a given list.

Since the number of points is small (up to 50), a brute-force approach is feasible and efficient enough. The idea is to check every possible combination of three points, calculate the area of the triangle they form, and keep track of the maximum area found.

1.  **Iterate Through Combinations**:
    We need to select every unique triplet of points from the input list. This can be done using three nested loops or more cleanly with Python's `itertools.combinations(points, 3)`.

2.  **Calculate Triangle Area**:
    For each triplet of points (p1, p2, p3), where p1=(x1, y1), p2=(x2, y2), and p3=(x3, y3), we can calculate the area using the Shoelace formula (also known as the Surveyor's formula). The formula is:
    Area = 0.5 * |x1(y2 - y3) + x2(y3 - y1) + x3(y1 - y2)|

3.  **Track Maximum Area**:
    Initialize a variable `max_area` to 0.0. After calculating the area for each triplet, update `max_area` if the current area is larger.

4.  **Return Result**:
    After checking all combinations, `max_area` will hold the area of the largest possible triangle.

The time complexity will be O(n^3) due to iterating through all triplets of points, which is acceptable for n <= 50. The space complexity is O(1).
"""

from typing import List
from itertools import combinations

class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        max_area = 0.0

        # Iterate through all unique combinations of 3 points
        for p1, p2, p3 in combinations(points, 3):
            x1, y1 = p1
            x2, y2 = p2
            x3, y3 = p3

            # Calculate area using the Shoelace formula
            curr_area = abs(
                0.5 * (x1*(y2-y3) + x2*(y3-y1) + x3*(y1-y2))
            )
            max_area = max(max_area, curr_area)

        return max_area

# --- Testing System ---
def test_solution(func, test_cases):
    for idx, (input_val, expected) in enumerate(test_cases, 1):
        output = func(input_val)
        # Using a tolerance for float comparison
        if abs(output - expected) < 1e-5:
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
        ([[0,0],[0,1],[1,0],[0,2],[2,0]], 2.0),
        ([[1,0],[0,0],[0,1]], 0.5),
        ([[4,6],[6,5],[3,1]], 5.5)
    ]
    
    test_solution(sol.largestTriangleArea, test_cases)