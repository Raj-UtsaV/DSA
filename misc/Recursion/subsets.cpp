#include <iostream>
#include<vector>
#include <algorithm>
#define llu long long unsigned
using namespace std;

void solve(vector<int> nums,vector<int> output,llu int index,vector<vector<int>> &ans){
    
    // todo Base case
    if(index >= nums.size()){
        sort(output.begin(),output.end());
        ans.push_back(output);
        return;
    }

    //todo Exclude
    solve(nums, output, index + 1, ans);

    //todo Include
    int element = nums[index];
    output.push_back(element);
    solve(nums, output, index + 1, ans);
}
 
int main() {
    vector<int> nums = {1, 2, 3};
    vector<vector<int>> ans;
    vector<int> output;
    llu int index = 0;
    solve(nums, output, index, ans);

    for (llu int i = 0; i < ans.size(); i++)
    {
        for (llu int j = 0; j < ans[i].size();j++){
            cout << ans[i][j] << " ";
        }
        cout << endl;
    }
    return 0;
}