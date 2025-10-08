"""
Problem Description:
--------------------
LeetCode 2300. Successful Pairs of Spells and Potions
Link: https://leetcode.com/problems/successful-pairs-of-spells-and-potions/

You are given two positive integer arrays `spells` and `potions` of lengths `n` and `m` respectively, where `spells[i]`
represents the strength of the `i`th spell and `potions[j]` represents the strength of the `j`th potion.

You are also given an integer `success`. A spell and potion pair `(spells[i], potions[j])` is considered successful if the
product of their strengths is at least `success`.

Return an integer array `pairs` of length `n` where `pairs[i]` is the number of potions that will form a successful pair
with the `i`th spell.

Example:
--------
Input: spells = [5,1,3], potions = [1,2,3,4,5], success = 7
Output: [4,0,3]
Explanation:
- The 1st spell (5) with potions [1,2,3,4,5] gives products [5,10,15,20,25]. 4 of these are >= 7.
- The 2nd spell (1) with potions [1,2,3,4,5] gives products [1,2,3,4,5]. 0 of these are >= 7.
- The 3rd spell (3) with potions [1,2,3,4,5] gives products [3,6,9,12,15]. 3 of these are >= 7.
Thus, [4,0,3] is returned.

"""

#!IDEA
"""
A brute-force approach would involve checking every spell against every potion, resulting in an O(n*m) time complexity, which
is likely too slow given the constraints.

A more optimal approach involves sorting and binary search.

--- Solution 1: Sorting and Binary Search ---
* Core Logic:
    1.  **Sort Potions**: First, sort the `potions` array. This allows us to use binary search efficiently.
    2.  **Iterate Through Spells**: For each `spell` in the `spells` array:
        a.  **Calculate Minimum Potion Strength**: Determine the minimum potion strength required to achieve the `success`
            value. If `spell * potion >= success`, then `potion >= success / spell`.
            To handle integer division correctly for the ceiling value, we can calculate the required potion strength as
            `min_potion = (success + spell - 1) // spell`.
        b.  **Binary Search**: Use binary search (specifically `bisect_left`) on the sorted `potions` array to find the
            index of the first potion whose strength is greater than or equal to `min_potion`.
        c.  **Count Successful Pairs**: If `bisect_left` returns an index `j`, it means that `potions[j]` and all subsequent
            potions will form a successful pair with the current spell. The number of such potions is `len(potions) - j`.
    3.  **Collect Results**: Append this count to the result array for each spell.

* Complexity:
    - Time complexity: O(m log m + n log m), where `n` is the length of `spells` and `m` is the length of `potions`.
      O(m log m) for sorting `potions` and O(n * log m) for iterating through `spells` and performing a binary search for each.
    - Space complexity: O(1) or O(n) depending on whether the result array is counted as extra space.

--- Solution 2: Brute Force (for comparison) ---
* Core Logic:
    1. Iterate through each `spell` in `spells`.
    2. For each `spell`, iterate through every `potion` in `potions`.
    3. If `spell * potion >= success`, increment a counter.
    4. After checking all potions, add the counter to the result.

* Complexity:
    - Time complexity: O(n * m).
    - Space complexity: O(1) or O(n).
"""

from typing import List
from bisect import bisect_left

class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        """Solution 1: Sorting and Binary Search"""
        ans = []
        potions.sort()
        m = len(potions)
        for spell_strength in spells:
            # Calculate the minimum potion strength required
            min_potion_strength = (success + spell_strength - 1) // spell_strength
            # Find the first potion that is strong enough
            j = bisect_left(potions, min_potion_strength)
            # All potions from index j to the end are successful
            ans.append(len(potions) - j)

        return ans

    def successfulPairs_brute(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        """Solution 2: Brute Force"""
        ans = []
        n = len(spells)
        m = len(potions)
        for i in range(n):
            count = 0
            for j in range(m):
                if spells[i] * potions[j] >= success:
                    count += 1
            ans.append(count)
        return ans


# --- Testing System ---
def test_solution(func, test_cases):
    for idx, (input_val, expected) in enumerate(test_cases, 1):
        spells, potions, s = input_val
        output = func(spells, potions, s)
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
        (([5, 1, 3], [1, 2, 3, 4, 5], 7), [4, 0, 3]),
        (([3, 1, 2], [8, 5, 8], 16), [2, 0, 2]),
    ]

    test_solution(sol.successfulPairs, test_cases)