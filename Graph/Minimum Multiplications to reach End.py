"""
Problem Description:
--------------------
[problem:] Minimum Multiplications to reach End
[link:] https://www.geeksforgeeks.org/problems/minimum-multiplications-to-reach-end/1
[description:] Given a start number, an end number, and an array of multipliers, find the minimum
number of multiplications to transform the start number to the end number. In each step, you can
multiply the current number by any element of the array. All multiplications are performed modulo 100000.

Example:
--------
Input: arr = [2, 5, 7], start = 3, end = 30
Output: 2
Explanation:
Step 1: 3 * 2 = 6
Step 2: 6 * 5 = 30

"""

#!IDEA
"""
This problem can be modeled as finding the shortest path in an unweighted graph.

--- Solution: Breadth-First Search (BFS) ---

*   **Graph Representation**:
    -   The nodes of the graph are the numbers from 0 to 99999.
    -   A directed edge exists from a number `u` to `v` if `v = (u * multiplier) % 100000` for some `multiplier` in the input array.
    -   Since each multiplication counts as one step, all edge weights are 1.

*   **Algorithm**:
    -   BFS is the perfect algorithm for finding the shortest path in an unweighted graph. We will explore the graph level by level, where each level corresponds to an additional multiplication step.

*   **State**:
    -   `dist`: An array of size 100000, where `dist[i]` stores the minimum number of multiplications needed to reach number `i` from the `start` number. We initialize all distances to infinity.
    -   `queue`: A queue to manage the BFS traversal. It will store tuples of `(number, steps)` to keep track of the current number and the steps taken to reach it.

*   **Core Logic**:
    1.  **Initialization**:
        -   If `start` equals `end`, 0 steps are needed.
        -   Initialize a `dist` array with a large value (infinity) to indicate that no node has been reached yet.
        -   Set `dist[start] = 0`.
        -   Push the starting state `(start, 0)` into the queue.

    2.  **BFS Traversal**:
        -   While the queue is not empty, dequeue the current `(node, steps)`.
        -   For each `multiplier` in the input `arr`:
            -   Calculate the `next_num = (node * multiplier) % 100000`.
            -   If we have found a shorter path to `next_num` (i.e., `steps + 1 < dist[next_num]`), it means this is the first time we are reaching `next_num` or we found a better path.
            -   Update `dist[next_num] = steps + 1`.
            -   If `next_num` is the `end` number, we have found the shortest path. Return `steps + 1`.
            -   Enqueue the new state `(next_num, steps + 1)` to explore from it later.

*   **Result**:
    -   If the `end` number is reached during the traversal, we return its distance.
    -   If the queue becomes empty and we haven't reached the `end` number, it means the `end` is unreachable. In this case, we return -1.

*   **Complexity**:
    -   Time Complexity: O(V * M), where V is the number of possible states (100000) and M is the size of the `arr`. In the worst case, we visit each number from 0 to 99999 and perform M multiplications for each.
    -   Space Complexity: O(V) for the `dist` array and the queue, which can hold up to V elements in the worst case.
"""

from typing import List
from collections import deque


class Solution:
    def minimumMultiplications(self, arr: List[int], start: int, end: int) -> int:
        if start == end:
            return 0

        mod = 100000
        dist = [float('inf')] * mod
        dist[start] = 0

        # The queue will store tuples of (number, steps)
        queue = deque([(start, 0)])

        while queue:
            node, steps = queue.popleft()

            for it in arr:
                num = (node * it) % mod

                # If we found a shorter path to `num`
                if steps + 1 < dist[num]:
                    dist[num] = steps + 1
                    # If we reached the end, return the steps immediately
                    if num == end:
                        return steps + 1
                    queue.append((num, steps + 1))

        # If the queue becomes empty and we haven't reached the end
        return -1


# --- Testing System ---
def test_solution(func, test_cases):
    for idx, (input_val, expected) in enumerate(test_cases, 1):
        # Unpack the input tuple
        arr, start, end = input_val
        output = func(arr, start, end)
        if output == expected:
            print(f"Test case {idx}: ✅ Passed")
        else:
            print(f"Test case {idx}: ❌ Failed")
            print(f"  Input: arr={arr}, start={start}, end={end}")
            print(f"  Output: {output}")
            print(f"  Expected: {expected}")


# --- Example Test Cases ---
if __name__ == "__main__":
    sol = Solution()
    test_cases = [
        (([2, 5, 7], 3, 30), 2),
        (([3, 4, 65], 7, 66175), 4),
        (([1], 10, 20), -1),
        (([7], 7, 7), 0),
    ]

    test_solution(sol.minimumMultiplications, test_cases)


"""
Dry Run Example:
---------------
Input: arr = [2, 5, 7], start = 3, end = 30

1. Init:
   - dist = [inf, inf, inf, 0, inf, ...] (dist[3] = 0)
   - queue = deque([(3, 0)])

2. Pop (3, 0). node=3, steps=0.
   - it=2: num = (3*2)%mod = 6. dist[6] is inf. Update dist[6]=1. Push (6, 1).
   - it=5: num = (3*5)%mod = 15. dist[15] is inf. Update dist[15]=1. Push (15, 1).
   - it=7: num = (3*7)%mod = 21. dist[21] is inf. Update dist[21]=1. Push (21, 1).
   - queue = [(6, 1), (15, 1), (21, 1)]

3. Pop (6, 1). node=6, steps=1.
   - it=2: num = (6*2)%mod = 12. dist[12]=2. Push (12, 2).
   - it=5: num = (6*5)%mod = 30. dist[30]=2.
     - num == end (30 == 30). ✅ Return steps + 1 = 1 + 1 = 2.

Algorithm terminates and returns 2.
"""