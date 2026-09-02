"""Canonical solution metadata.

Problem Number: 611
Problem Title: Valid Triangle Number
Platform: LeetCode
Difficulty: Medium
Official Platform Topics: Array, Two Pointers, Binary Search, Greedy, Sorting
Study Tags: Sorted two pointers
Canonical URL: https://leetcode.com/problems/valid-triangle-number/
"""

"""
Problem Description:
--------------------
LeetCode 611. Valid Triangle Number
Link: https://leetcode.com/problems/valid-triangle-number/

Given an integer array nums, return the number of triplets chosen from the array that can make triangles if we take them as side lengths of a triangle.

A triplet (a, b, c) can form a triangle if a + b > c, a + c > b, and b + c > a.

Example:
--------
Input: nums = [2,2,3,4]
Output: 3
Explanation:
Valid combinations are:
2,3,4 (using the first 2)
2,3,4 (using the second 2)
2,2,3

"""

#!IDEA
"""
The problem asks us to find the number of triplets (a, b, c) from the array that can form a triangle. The condition for forming a triangle is that the sum of any two sides must be greater than the third side.

A naive approach would be to use three nested loops to check every possible triplet, which would be O(n^3) and likely too slow.

A more efficient approach involves sorting and using two pointers:
1.  **Sort the Array**: First, sort the input array `nums`. This is a key step. If we have three sides `a, b, c` such that `a <= b <= c`, we only need to check if `a + b > c`. The other two conditions (`a + c > b` and `b + c > a`) will automatically be true because `c` is the largest side.

2.  **Iterate and Use Two Pointers**:
    - We iterate from the end of the sorted array to select the largest side `c` of a potential triangle. Let's say `c` is at index `k`.
    - For each `c` (i.e., `nums[k]`), we need to find pairs `(a, b)` from the subarray `nums[0...k-1]` such that `a + b > c`.
    - We can do this efficiently using two pointers, `i` starting at `0` and `j` starting at `k-1`.

3.  **Two-Pointer Logic**:
    - While `i < j`:
        - If `nums[i] + nums[j] > nums[k]`: We have found a valid pair `(nums[i], nums[j])`. Since the array is sorted, any element between `i` and `j` (i.e., `nums[i+1], nums[i+2], ..., nums[j-1]`) when paired with `nums[j]` will also form a valid triangle with `nums[k]`. For example, `nums[i+1] + nums[j] > nums[i] + nums[j] > nums[k]`.
        - Therefore, all pairs `(nums[i], nums[j])`, `(nums[i+1], nums[j])`, ..., `(nums[j-1], nums[j])` are valid. The number of such pairs is `j - i`.
        - We add `j - i` to our count and decrement `j` to try a smaller second side `b`.
        - If `nums[i] + nums[j] <= nums[k]`: The sum is too small. To increase the sum, we must use a larger first side `a`, so we increment `i`.

4.  **Complexity**: Sorting takes O(n log n). The nested loops (the `for` loop for `k` and the `while` loop for `i, j`) give a complexity of O(n^2). The overall time complexity is dominated by the O(n^2) part. The space complexity is O(1) (or O(n) depending on the sort implementation).
"""

from typing import List

class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()
        cnt = 0
        n = len(nums)
        # Iterate from the end to fix the largest side 'c' of the triangle
        for k in range(n-1,-1,-1):
            # Use two pointers to find pairs (a, b) such that a + b > c
            i,j = 0,k-1
            while i < j:
                # If nums[i] + nums[j] > nums[k], we have a valid triangle.
                # All elements from i to j-1 will also form a valid triangle with nums[j].
                # For example, (nums[i], nums[j], nums[k]), (nums[i+1], nums[j], nums[k]), ...
                if nums[i] + nums[j] > nums[k]:
                    # There are (j - i) such valid pairs.
                    cnt += (j-i)
                    # Try a smaller second side 'b'
                    j-=1
                else:
                    # The sum is too small, we need a larger first side 'a'
                    i+=1

        return cnt

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
        ([2,2,3,4], 3),
        ([4,2,3,4], 4),
        ([0,0,0], 0),
        ([1,2,3,4,5,6], 7)
    ]

    test_solution(sol.triangleNumber, test_cases)