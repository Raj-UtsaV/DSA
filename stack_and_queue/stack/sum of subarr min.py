"""
Problem Description:
--------------------
[problem:] LeetCode 907. Sum of Subarray Minimums
[link:] https://leetcode.com/problems/sum-of-subarray-minimums/
[Brief description of the problem, input/output requirements, constraints, and examples]
Given an array of integers arr, find the sum of min(b) for every (contiguous) subarray b of arr.
Since the answer may be large, return the answer modulo 10^9 + 7.

Example:
--------
Input: arr = [3,1,2,4]
Output: 17
Explanation:
Subarrays are [3], [1], [2], [4], [3,1], [1,2], [2,4], [3,1,2], [1,2,4], [3,1,2,4].
Minimums are 3, 1, 2, 4, 1, 1, 2, 1, 1, 1.
Sum is 17.

"""

#!IDEA
"""
The core idea is to calculate the contribution of each element `arr[i]` to the total sum.
An element `arr[i]` is the minimum in a subarray `arr[j..k]` where `j <= i <= k`.
The number of such subarrays is `(number of possible start indices j) * (number of possible end indices k)`.

To find these counts, we need to find the boundaries for each `arr[i]`. To handle duplicates correctly, we must define the boundaries asymmetrically. We can define `arr[i]` as the minimum if it's strictly smaller than elements to its left and smaller than or equal to elements to its right.

- Left Boundary: Find the index of the first element to the left of `i` that is strictly smaller than `arr[i]`. Let's call this `psee[i]` (Previous Strictly Smaller Element).
- Right Boundary: Find the index of the first element to the right of `i` that is smaller than or equal to `arr[i]`. Let's call this `nse[i]` (Next Smaller or Equal Element).

So, for `arr[i]`, the valid start indices `j` can be from `psee[i] + 1` to `i`. The number of choices is `i - psee[i]`.
The valid end indices `k` can be from `i` to `nse[i] - 1`. The number of choices is `nse[i] - i`.

The total number of subarrays where `arr[i]` is the designated minimum is `(i - psee[i]) * (nse[i] - i)`.
The contribution of `arr[i]` to the final sum is `arr[i] * (i - psee[i]) * (nse[i] - i)`.

We can compute `psee` and `nse` arrays efficiently in O(n) time using a monotonic stack.

1.  **`psee` (Previous Strictly Smaller):** Iterate from left to right. Use a stack to keep track of indices. For `arr[i]`, pop from the stack while `arr[stack.top()] >= arr[i]`. The top of the stack is then the index of the previous strictly smaller element.
2.  **`nse` (Next Smaller or Equal):** Iterate from right to left. Use a stack to keep track of indices. For `arr[i]`, pop from the stack while `arr[stack.top()] > arr[i]`. The top of the stack is then the index of the next smaller or equal element.

The provided code implements this logic.
"""

from typing import List

class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        n = len(arr)
        mod = 10**9 + 7

        # nse: Next Smaller or Equal Element
        # For each arr[i], find the index of the next element to the right that is <= arr[i].
        nse = [n] * n
        stack = []
        for i in range(n-1, -1, -1):
            # Pop elements from stack that are strictly greater than arr[i]
            while stack and arr[stack[-1]] > arr[i]:
                stack.pop()
            # The top of the stack is now the next smaller or equal element
            nse[i] = stack[-1] if stack else n
            stack.append(i)

        # psee: Previous Strictly Smaller Element
        # For each arr[i], find the index of the element to the left that is < arr[i].
        psee = [-1] * n
        stack = []
        for i in range(n):
            # Pop elements from stack that are greater than or equal to arr[i]
            while stack and arr[stack[-1]] >= arr[i]:
                stack.pop()
            # The top of the stack is now the previous strictly smaller element
            psee[i] = stack[-1] if stack else -1
            stack.append(i)

        # Calculate sum of contributions
        total = 0
        for i in range(n):
            left = i - psee[i]
            right = nse[i] - i
            total = (total + arr[i] * left * right) % mod

        return total

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
        ([3, 1, 2, 4], 17),
        ([11, 81, 94, 43, 3], 444),
        ([2, 2], 6),
    ]
    
    test_solution(sol.sumSubarrayMins, test_cases)

"""
Dry Run Example:
---------------
Input: arr = [3, 1, 2, 4]

🎯 Start

1. #! Calculate psee (Previous Strictly Smaller)
   - i=0, arr[0]=3: stack=[], psee[0]=-1, stack=[0]
   - i=1, arr[1]=1: stack=[0], arr[0]>=arr[1], pop 0. stack=[], psee[1]=-1, stack=[1]
   - i=2, arr[2]=2: stack=[1], arr[1]>=arr[2] is false. psee[2]=1, stack=[1,2]
   - i=3, arr[3]=4: stack=[1,2], arr[2]>=arr[3] is false. psee[3]=2, stack=[1,2,3]
   => psee = [-1, -1, 1, 2]

2. #! Calculate nse (Next Smaller or Equal)
   - i=3, arr[3]=4: stack=[], nse[3]=4, stack=[3]
   - i=2, arr[2]=2: stack=[3], arr[3]>arr[2], pop 3. stack=[], nse[2]=4, stack=[2]
   - i=1, arr[1]=1: stack=[2], arr[2]>arr[1], pop 2. stack=[], nse[1]=4, stack=[1]
   - i=0, arr[0]=3: stack=[1], arr[1]>arr[0] is false. nse[0]=1, stack=[1,0]
   => nse = [1, 4, 4, 4]

3. #! Calculate Total Sum
   - i=0 (arr[0]=3): left=0-(-1)=1, right=1-0=1. contrib = 3*1*1=3. total=3
   - i=1 (arr[1]=1): left=1-(-1)=2, right=4-1=3. contrib = 1*2*3=6. total=9
   - i=2 (arr[2]=2): left=2-1=1, right=4-2=2. contrib = 2*1*2=4. total=13
   - i=3 (arr[3]=4): left=3-2=1, right=4-3=1. contrib = 4*1*1=4. total=17

✅ Final Answer: 17
"""