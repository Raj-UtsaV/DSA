#include <iostream>
#include <vector>
#include <stack>
#define llu long long unsigned
using namespace std;

vector<int> NGE2_brute(vector<int> v)
{
    vector<int> res(v.size(), -1);
    for (llu i = 0; i < v.size(); i++)
    {
        for (llu j = i + 1; j < (i + v.size()); j++)
        {   

            int index = j % v.size(); //? if you traversing the array thice without the doubling it 
            if (v[index] > v[i])
            {
                res[i] = v[index];
                break;
            }
        }
    }
    return res;
}

vector<int> NGE2_optimal(vector<int> v)
{
    vector<int> res(v.size(), -1);
    stack<int> s;
    for (llu i = 0; i < 2 * v.size(); i++)
    {
        int index = i % v.size();

        
        while (!s.empty() && v[index] > v[s.top()])
        {
            res[s.top()] = v[index]; 
            s.pop();                 
        }

        
        if (i < v.size())
        {
            s.push(index); 
        }
    }
    return res;
}
int main()
{
    vector<int> nums = {1, 2, 1};
    vector<int> ans = NGE2_brute(nums);
    for (llu i = 0; i < ans.size(); i++)
        cout << ans[i] << " ";
    cout << endl;
    ans = NGE2_optimal(nums);
    for (llu i = 0; i < ans.size(); i++)
        cout << ans[i] << " ";

    return 0;
}