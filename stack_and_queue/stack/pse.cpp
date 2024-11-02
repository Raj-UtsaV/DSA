#include <iostream>
#include <vector>
#include <stack>
#define llu long long unsigned
using namespace std;

vector<int> PSE_brute(vector<int> v)
{
    vector<int> res(v.size(), -1);
    for (int i = v.size() - 1; i >= 0; i--)
    {
        for (int j = i - 1; j >= 0; j--)
        {
            if (v[j] < v[i])
            {
                res[i] = v[j];
                break;
            }
        }
    }
    return res;
}

vector<int> PSE_optimal(vector<int> v)
{
    vector<int> ans(v.size(), -1);
    stack<int> s;
    s.push(v[0]);
    v.size();
    for (int i = 1; i < v.size(); i++)
    {
        if (v[i] > s.top())
        {
            ans[i] = s.top();
            s.push(v[i]);
        }
        else
        {
            while (!s.empty() && v[i] <= s.top())
            {
                s.pop();
            }
            if (!s.empty())
            {
                ans[i] = s.top();
            }
            s.push(v[i]);
        }
    }

    return ans;
}
int main()
{
    vector<int> v = {4, 5, 2, 10, 8};
    vector<int> result = PSE_brute(v);
    for (int i = 0; i < result.size(); i++)
    {
        cout << result[i] << " ";
    }
    cout << endl;
    result = PSE_optimal(v);
    for (int i = 0; i < result.size(); i++)
    {
        cout << result[i] << " ";
    }
    return 0;
}