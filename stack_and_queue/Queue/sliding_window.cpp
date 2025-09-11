#include<iostream>
#include<vector>
#include<deque>
#define llu long long unsigned
using namespace std;


vector<int> brute(vector<int> arr,int k){
    vector<int> ans;
    for (llu i = 0;i<=arr.size()-k;i++){
        int maxi = arr[i];
        for (llu j = i; j <= i + k-1;j++){
            maxi = max(maxi, arr[j]);
        }
        ans.push_back(maxi);
    }
    return ans;
}

vector<int> optimal(vector<int> &nums, int k)
{
    deque<int> dq;
    vector<int> ans;
    for (int i = 0; i < nums.size(); i++)
    {
        if (!dq.empty() && dq.front() == i - k)
            dq.pop_front();

        while (!dq.empty() && nums[dq.back()] < nums[i])
            dq.pop_back();

        dq.push_back(i);
        if (i >= k - 1)
            ans.push_back(nums[dq.front()]);

        cout << endl;
    }
    return ans;
}




void print(vector<int> ans){
    for (llu i = 0; i < ans.size(); i++)
    {
        cout << ans[i] << " ";
    }
    cout << endl;
}


int main(){
    vector<int> v = {1, 3, -1, -3, 5, 3, 6, 7};
    int k = 3;
    vector<int> ans = brute(v, k);
    print(ans);
    ans = optimal(v, k);
    print(ans);
    return 0;
}