#include <iostream>
#include <vector>
#include <stack>
#include <algorithm>
using namespace std;

vector<int> boom(vector<int> v)
{
    stack<int> s;
    vector<int> result;
    for (int i = 0; i < v.size(); i++)
    {
        if (v[i] > 0) // If the current element is positive
        {
            s.push(v[i]); // Push it onto the stack
        }
        else
        { // If the current element is negative
            while (!s.empty() && s.top() < -1 * v[i] && s.top() > 0)
            {
                s.pop(); // Pop elements from the stack while top is less than the current negative element
            }
            if (!s.empty() && s.top() == abs(v[i]))
            {
                s.pop(); // If the top of the stack is the absolute value of the current element, pop it
            }
            else if (s.empty() || s.top() < 0)
            {
                s.push(v[i]); // If stack is empty or top is negative, push the current element
            }
        }
    }
    {
    }
    while (!s.empty())
    {
        result.push_back(s.top());
        s.pop();
    }
    reverse(result.begin(), result.end());
    return result;
}

int main()
{
    vector<int> v1 = {10, 2, -5};
    vector<int> v = boom(v1);
    for (int i = 0; i < v.size(); i++)
    {
        cout << v[i] << " ";
    }
    return 0;
}