#include <iostream>
#include<vector>
#include<set>
#include<unordered_map>
using namespace std;
 

int brute(vector<int> &arr){
    int n = arr.size();
    int maxlen = 0;
    for (int i = 0; i < n; i++)
    {
        set<int> s;
        int j = i;
        while (j < n)
        {
            s.insert(arr[j]);
            if (s.size() <= 2)
                maxlen = max(maxlen, j - i + 1);
            else
                break;
            j++;
        }
    }
    return maxlen;
}

int better(vector<int> &nums){
    int n = nums.size();
    int maxlen = 0;
    int left = 0;
    unordered_map<int, int> mpp;
    int right = 0;
    while (right < n)
    {
        mpp[nums[right]]++;
        while (mpp.size() > 2)
        {
            mpp[nums[left]]--;
            if (mpp[nums[left]] == 0)
                mpp.erase(nums[left]);
            left++;
        }
        maxlen = max(maxlen, right - left + 1);
        right++;
    }
    return maxlen;
}

int optimal(vector<int> &arr){
    int n = arr.size();
    int maxlen = 0;
    int left = 0;
    int right = 0;
    unordered_map<int, int> mpp;
    while (right < n)
    {
        mpp[arr[right]]++;
        if(mpp.size()>2){
            mpp[arr[left]]--;
            if(mpp[arr[left]] == 0)
                mpp.erase(arr[left]);
            left++;
        }
        if(mpp.size()<=2)
            maxlen = max(maxlen, right - left + 1);
        right++;
    }
    return maxlen;
}
int main() {
    vector<int> nums = {2, 1, 2};
    cout << brute(nums) << endl; // Output: 3
    cout << better(nums) << endl; // Output: 3
    cout << optimal(nums) << endl; // Output: 3

    return 0;
}