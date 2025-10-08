"""
Problem Description:
--------------------
LeetCode 1488. Avoid Flood in The City
Link: https://leetcode.com/problems/avoid-flood-in-the-city/

You are given an integer array rains where:
- rains[i] > 0 means on day i, it rains in lake rains[i].
- rains[i] == 0 means on day i, there is no rain, and you can choose one lake to dry.

Return an array `ans` where:
- ans[i] = -1 if it rains on day i.
- ans[i] = k if you choose to dry lake k on day i.
- ans[i] = 1 (or any positive integer) for unused dry days.

If it's impossible to avoid a flood, return an empty array. A flood occurs if it rains in a lake that is already full.

Example:
--------
Input: rains = [1,2,0,0,2,1]
Output: [-1,-1,2,1,-1,-1]
Explanation: On day 0, lake 1 is full. On day 1, lake 2 is full. On day 2, we have a dry day, we can dry any lake, let's dry lake 2. On day 3, we have another dry day, let's dry lake 1. On day 4, it rains in lake 2, which is empty. On day 5, it rains in lake 1, which is empty.

"""

#!IDEA
"""
The problem requires us to make a greedy choice on dry days to prevent future floods.
When a lake is about to flood, we need to use a dry day that occurred between the last time it rained in that lake and the current day. To save "better" dry days (later ones) for future potential floods, the greedy choice is to always use the *earliest possible* dry day.

--- Solution 1: Greedy with Binary Search (Optimized) ---
* State:
    - `full_lakes`: A dictionary mapping a lake number to the day it was last filled. `full_lakes = {lake: day}`.
    - `dry_days`: A sorted list of indices representing the days we can use to dry a lake.
    - `ans`: The result array, initialized with dummy values.

* Core Logic:
    1.  **Iterate through `rains` day by day**:
        - For each day `i` and lake `n = rains[i]`:

    2.  **Handle Dry Days (n == 0)**:
        - If it's a dry day, we don't know which lake is best to dry yet. The best strategy is to save this dry day for a future emergency.
        - We add the day's index `i` to our `dry_days` list.
        - We can put a placeholder in the answer, like `ans[i] = 1`, for now.

    3.  **Handle Rainy Days (n > 0)**:
        - Mark `ans[i] = -1` as we can't do anything else on a rainy day.
        - **Check for Flood Condition**: Check if the current lake `n` is already in `full_lakes`.
            - If it is, a flood is imminent. We must find a dry day that occurred *after* the lake was last filled (`last_fill_day = full_lakes[n]`) but *before* the current day `i`.
            - To make the best greedy choice, we should use the *earliest possible* dry day after `last_fill_day`. This saves later dry days for floods that might happen even later.
            - We can efficiently find this earliest dry day by performing a binary search (`bisect_right`) on our sorted `dry_days` list to find the first dry day index `d` where `dry_days[d] > last_fill_day`.
            - **If no such dry day exists** (binary search doesn't find a suitable day), a flood is unavoidable. Return `[]`.
            - **If a dry day is found**:
                - Use it: Set `ans[dry_days[d]] = n`.
                - Remove it: This dry day is now used, so remove it from `dry_days`.
        - **Update Lake Status**: In either case (flood averted or first-time rain), update the last filled day for the current lake: `full_lakes[n] = i`.

* Result:
    - If the loop completes without returning `[]`, it means we successfully avoided all floods. The `ans` array contains the valid sequence of actions.

* Complexity:
    - Time complexity: O(N * D) in the worst case, where N is the number of days and D is the number of dry days. The `bisect_right` operation is O(log D), but `dry_days.pop(idx)` is an O(D) operation on a list. While the search is fast, the removal dominates this part of the complexity.
    - Space complexity: O(N) for storing `full_lakes`, `dry_days`, and `ans`.

--- Solution 2: Greedy with Linear Scan (Original Approach) ---
This approach follows the same greedy logic but uses a simpler data structure for dry days.

* State:
    - `full_lakes`: A dictionary mapping a lake number to the day it was last filled.
    - `dry_days`: A simple list (not necessarily sorted) of available dry day indices.
    - `ans`: The result array.

* Core Logic:
    1.  **Dry Days**: When `rains[i] == 0`, append `i` to the `dry_days` list.
    2.  **Rainy Days**: When `rains[i] > 0`:
        - If the lake `n` is already full (i.e., in `full_lakes`):
            - We must find a dry day to use. We linearly scan through our `dry_days` list.
            - We look for the first `dry_day_index` that is greater than the `last_fill_day` of lake `n`.
            - **If found**: We use that day (set `ans[dry_day_index] = n`) and remove it from `dry_days` using `pop()`.
            - **If not found**: A flood is unavoidable. Return `[]`.
        - Update the last filled day for lake `n`: `full_lakes[n] = i`.

* Complexity:
    - Time complexity: O(N * D). For each rainy day on a full lake, we might scan the entire `dry_days` list (O(D)) and then `pop` an element (also O(D)).
    - Space complexity: O(N).

Both solutions have a similar worst-case time complexity, but the binary search approach will be faster on average as it avoids a full linear scan to find the correct dry day.
"""

from typing import List
import bisect

class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        """Solution 1: Greedy with Binary Search"""
        # {lake_number: day_it_was_filled_on}
        full_lakes = {}
        # A sorted list of available dry days
        dry_days = []
        ans = [-1]*len(rains)

        for i, n in enumerate(rains):
            if n == 0:
                # It's a dry day, save its index for later use.
                dry_days.append(i)
                ans[i] = 1  # Dummy value for now, can be overwritten.
            else:
                # It's a rainy day.
                if n in full_lakes:
                    # This lake is already full. We must dry it.
                    last_fill_day = full_lakes[n]
                    
                    # Find the earliest dry day after the last fill day.
                    # bisect_right finds an insertion point which comes after (to the right of)
                    # any existing entries of last_fill_day in dry_days.
                    idx = bisect.bisect_right(dry_days, last_fill_day)
                    
                    if idx == len(dry_days):
                        # No available dry day found after the lake was filled. Flood!
                        return []
                    
                    # Use the found dry day
                    dry_day_to_use = dry_days[idx]
                    ans[dry_day_to_use] = n
                    dry_days.pop(idx)
                
                # Update the last day this lake was filled.
                full_lakes[n] = i

        return ans

    def avoidFlood_linear_scan(self, rains: List[int]) -> List[int]:
        """Solution 2: Greedy with Linear Scan"""
        # map the filling day of pond with day no.
        Track_Full_day = {}
        # Track the empty day with day no.
        Track_empty_day = []

        ans = [-1]*len(rains)

        for i, n in enumerate(rains):
            if n == 0:
                # put the day of dry in Track_empty
                Track_empty_day.append(i)
                ans[i] = 1 ##dummy marking

            else:
                if n in Track_Full_day:
                    #find the last filling day of the pond
                    last_fill_day = Track_Full_day[n]

                    # if a dry day found after the last_fill_day\
                    # then we can day that pond 

                    Found  = False

                    for j,dry_day in enumerate(Track_empty_day):
                        if dry_day > last_fill_day:
                            Found = True
                            ans[dry_day] = n 
                            Track_empty_day.pop(j)
                            break

                    if not Found:
                        return []
                    
                Track_Full_day[n] = i # even if you dry prev it filled todayn
            
        return ans


def test_solution(func, test_cases):
    for idx, (input_val, expected) in enumerate(test_cases, 1):
        output = func(input_val)
        # A specific valid output is expected, so direct comparison is fine.
        if output == expected:
            print(f"Test case {idx}: ✅ Passed")
        else:
            print(f"Test case {idx}: ❌ Failed")
            print(f"  Input: {input_val}")
            print(f"  Output: {output}")
            print(f"  Expected: {expected}")

# Example usage:
if __name__ == "__main__":
    sol = Solution()
    test_cases = [
        ([1,2,0,0,2,1], [-1,-1,2,1,-1,-1]),
        ([1,2,0,1,2], []),
        ([69,0,0,0,69], [-1,69,1,1,-1]),
        ([10,20,20], []),
        ([0,1,0,1,0,1], [1,-1,1,-1,1,-1]), # Example where ans[dry_day] is overwritten
    ]

    print("--- Testing Optimized Solution (Binary Search) ---")
    test_solution(sol.avoidFlood, test_cases)
    print("\n--- Testing Original Solution (Linear Scan) ---")
    test_solution(sol.avoidFlood_linear_scan, test_cases)
