/*
Problem Description:
--------------------
LeetCode 735. Asteroid Collision
Link: https://leetcode.com/problems/asteroid-collision/

We are given an array `asteroids` of integers representing asteroids in a row.
For each asteroid, the absolute value represents its size, and the sign represents its direction (positive meaning right, negative meaning left). All asteroids are moving at the same speed.
Find out the state of the asteroids after all collisions. If two asteroids meet, the smaller one will explode. If both are the same size, both will explode. Two asteroids moving in the same direction will never meet.

Example:
--------
Input: asteroids = [5, 10, -5]
Output: [5, 10]
Explanation: The 10 and -5 collide resulting in 10. The 5 and 10 never collide.

Input: asteroids = [10, 2, -5]
Output: [10]
*/

/*!IDEA
*   We can use a stack to simulate the collisions. The stack will store the asteroids that are moving and haven't collided yet.
*
*   Iterate through the input `asteroids` array one by one.
*
*   1.  If the current asteroid is positive (moving right), it won't collide with anything in the stack (as they are also moving right or the stack is empty). So, we push it onto the stack.
*
*   2.  If the current asteroid is negative (moving left), it might collide with the asteroids in the stack (which are all positive, moving right).
*       - We check the top of the stack.
*       - While the stack is not empty, its top is positive, and the top asteroid is smaller than the current (absolute value) negative asteroid, the top asteroid explodes. So, we pop it from the stack and continue checking.
*       - After the loop, there are three possibilities for the current negative asteroid:
*           a. If the stack is not empty and its top is positive and has the same size as the current negative asteroid, both explode. So, we pop the stack's top.
*           b. If the stack is empty or its top is negative, it means the current negative asteroid survived all collisions (or there were no right-moving asteroids to collide with). So, we push the current negative asteroid onto the stack.
*           c. If the stack top is positive and larger, the current negative asteroid explodes and we do nothing.
*
*   3.  After iterating through all asteroids, the stack contains the final state of the asteroids. We just need to convert the stack to a vector. Since the stack is LIFO, we'll need to reverse the order to get the correct sequence.
*/

#include <iostream>
#include <vector>
#include <stack>
#include <algorithm>
using namespace std;

class Solution {
public:
    vector<int> asteroidCollision(vector<int>& asteroids) {
        stack<int> s;
        for (int ast : asteroids) {
            if (ast > 0) {
                s.push(ast);
            } else { 
                bool destroyed = false;
                while (!s.empty() && s.top() > 0) {
                    if (s.top() < -ast) { // s.top() is smaller, it explodes
                        s.pop();
                        continue; // current asteroid continues to check
                    } else if (s.top() == -ast) { // same size, both explode
                        s.pop();
                        destroyed = true;
                        break;
                    } else { // s.top() > -ast, current asteroid explodes
                        destroyed = true;
                        break;
                    }
                }
                if (!destroyed) {
                    s.push(ast);
                }
            }
        }

        vector<int> result;
        while (!s.empty()) {
            result.push_back(s.top());
            s.pop();
        }
        reverse(result.begin(), result.end());
        return result;
    }
};

// --- Testing System ---
void test_solution(const vector<pair<vector<int>, vector<int>>>& test_cases) {
    Solution sol;
    for (size_t i = 0; i < test_cases.size(); ++i) {
        vector<int> input = test_cases[i].first;
        vector<int> expected = test_cases[i].second;
        vector<int> output = sol.asteroidCollision(input);

        cout << "Test case " << i + 1 << ": ";
        if (output == expected) {
            cout << "✅ Passed" << endl;
        } else {
            cout << "❌ Failed" << endl;
            cout << "  Input:    [";
            for(size_t j=0; j<input.size(); ++j) cout << input[j] << (j == input.size()-1 ? "" : ", ");
            cout << "]" << endl;

            cout << "  Output:   [";
            for(size_t j=0; j<output.size(); ++j) cout << output[j] << (j == output.size()-1 ? "" : ", ");
            cout << "]" << endl;

            cout << "  Expected: [";
            for(size_t j=0; j<expected.size(); ++j) cout << expected[j] << (j == expected.size()-1 ? "" : ", ");
            cout << "]" << endl;
        }
    }
}

int main()
{
    vector<pair<vector<int>, vector<int>>> test_cases = {
        {{5, 10, -5}, {5, 10}},
        {{8, -8}, {}},
        {{10, 2, -5}, {10}},
        {{-2, -1, 1, 2}, {-2, -1, 1, 2}}
    };

    test_solution(test_cases);

    return 0;
}

/*
Dry Run Example:
---------------
Input: asteroids = [10, 2, -5]

stack: []

1. i = 0, asteroid = 10 (positive)
   - Push 10 to stack.
   - stack: [10]

2. i = 1, asteroid = 2 (positive)
   - Push 2 to stack.
   - stack: [10, 2]

3. i = 2, asteroid = -5 (negative)
   - `while` loop: stack is not empty (top=2) and top > 0.
     - `s.top()` (2) < `-ast` (5). So pop 2.
     - stack: [10]. `continue` to next `while` iteration.
   - `while` loop: stack is not empty (top=10) and top > 0.
     - `s.top()` (10) is not < `-ast` (5).
     - `s.top()` (10) is not == `-ast` (5).
     - `else` branch: `s.top()` > `-ast`. `destroyed` becomes true. `break` from while.
   - `if (!destroyed)` is false. Nothing is pushed.
   - stack: [10]

Loop ends.

Convert stack to vector:
- Pop 10, result.push_back(10). result: [10]
- Reverse result. result: [10]

Return [10].
*/