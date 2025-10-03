"""
Problem Description:
--------------------
[problem:]
[link:]

[Brief description of the problem, input/output requirements, constraints, and examples]

Example:
--------
Input: [example input]
Output: [expected output]

"""

#!IDEA
"""
[Describe the overall approach/algorithm/logic for the problem]
- Mention the general technique(s) used (recursion, iteration, dynamic programming, backtracking, greedy, graph traversal, sorting, etc.).
- Explain the reasoning for choosing these approaches.

--- Solution 1: [Name of Approach] ---
* State:
    - Describe the key variables, parameters, or data structures used to track progress or state.
    - Explain why this state is sufficient.

* Base Case* (if applicable):
    - Explain stopping conditions or trivial cases.

* Core Logic:
    - Step-by-step description of the approach.
    - Important conditions or constraints to handle.

* Result:
    - How the final answer is derived from computed state or processing.

* Optimization* (if applicable):
    - Improvements to reduce time/space complexity (memoization, pruning, sorting, etc.).

* Complexity:
    - Time complexity.
    - Space complexity.

--- Solution 2: [Name of Alternative Approach] ---
* State:
    - Describe key state representation for this approach.

* Core Logic:
    - Step-by-step explanation.

* Result:
    - How the answer is derived.

* Optimization* (if applicable):
    - Improvements used.

* Complexity:
    - Time complexity.
    - Space complexity.

[Add more solutions if applicable]
"""


class Solution:
    def [function_name](self, [parameters]):
        # Initialize any results or helper data structures
        res = []

        # Define helper function if needed (e.g., recursive/backtracking function)
        def helper([arguments]):
            # Base case: check if solution is complete
            if [base_condition]:
                res.append([solution])
                return

            # Recursive/Iterative steps
            if [condition_1]:
                helper([updated arguments])
            
            if [condition_2]:
                helper([updated arguments])
            
            # Optional: any cleanup/backtracking steps

        # Start the helper
        helper([initial arguments])
        
        # Return the result
        return res


# --- Testing System ---
def test_solution(func, test_cases):
    for idx, (input_val, expected) in enumerate(test_cases, 1):
        output = func(input_val)
        # Sort both lists if order does not matter
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
        ([input_1], [expected_output_1]),
        ([input_2], [expected_output_2]),
        # Add more test cases
    ]
    
    test_solution(sol.[function_name], test_cases)


"""
Dry Run Example:
---------------
Input:  [
                [0, 1, 1],
                [1, 0, 1],
                [1, 1, 0]
            ], 3, True

🎯 Start Coloring

└── #!backtrack(0)
    └── #?is_safe(node=0, color=1) ✅ True
        🎨 assign color[0] = 1
        └── #!backtrack(1)
            ├── #?is_safe(node=1, color=1) ❌ False
            └── #?is_safe(node=1, color=2) ✅ True
                🎨 assign color[1] = 2
                └── #!backtrack(2)
                    ├── #?is_safe(node=2, color=1) ❌ False
                    ├── #?is_safe(node=2, color=2) ❌ False
                    └── #?is_safe(node=2, color=3) ✅ True
                        🎨 assign color[2] = 3
                        └── #!backtrack(3)
                            ├── #?is_safe(node=3, color=1) ❌ False
                            └── #?is_safe(node=3, color=2) ✅ True
                                🎨 assign color[3] = 2
                                ✅ SUCCESS → All vertices colored: [1, 2, 3, 2]




"""