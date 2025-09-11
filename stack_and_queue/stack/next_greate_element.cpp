#include <iostream>
#include <vector>
#include <stack>
#include<unordered_map>
#define llu long long unsigned
using namespace std;


vector<int> NGE_brute(vector<int> v){
    vector<int> ans(v.size(),-1) ;
    for (llu i = 0; i < v.size(); i++)
    {
        int x = 0;
        for (llu j = i + 1; j < v.size(); j++)
        {
            if (v[j] > v[i])
            {
                ans[i] = v[j];
                break;
            }
        }

    }
    return ans;
}

vector<int> NGE_optimal(vector<int> v){
    vector<int> ans(v.size(),-1) ;
    stack<int> s;
    s.push(v[v.size()-1]);
    for (int i = v.size() - 2; i >= 0; i--)
    {
        if(v[i]<s.top()){
            ans[i] = s.top();
            s.push(v[i]);
        }
        else{
            while(v[i]>s.top()){
                if (s.empty())
                    break;
                s.pop();
            }
            if(!s.empty()) ans[i] = s.top();
            s.push(v[i]);
        }
    }
    return ans;
}


void print(vector<int> ans){
    for (llu i = 0; i < ans.size(); i++)
        cout << ans[i] << " ";
    cout << endl;
}
int main()
{
    vector<int> v1 = {4, 1, 2};
    vector<int> v2 = {1, 3, 4, 2};
    vector<int> ans = NGE_brute(v2);
    print(ans);

    ans = NGE_optimal(v2);
    print(ans);

    return 0;
}
