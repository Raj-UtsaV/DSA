#include <iostream>
#include<vector>
using namespace std;
 
int brute(vector<int> nums,int k ){
    int maxlen = 0;
    for (int i = 0; i < nums.size(); i++)
    {
        int cnt = 0;
        for (int j = i; j < nums.size(); j++)
        {
            if (nums[j] == 0)
                cnt++;
            if (cnt <= k)
            {
                int len = j - i + 1;
                maxlen = max(maxlen, len);
            }
            else
                break;
        }
    }
    return maxlen;
}

int better(vector<int> nums,int k){
    int maxlen = 0;
    int l = 0, r = 0, cnt = 0;
    while (r < nums.size())
    {
        if (nums[r] == 0)
            cnt++;
        while (cnt > k)
        {
            if (nums[l] == 0)
                cnt--;
            l++;
        }
        int len = r - l + 1;
        maxlen = max(len, maxlen);
        r++;
    }
    return maxlen;
}


int main() {
    vector<int> nums = {1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0};
    int k = 2;
    cout << "Length of longest subarray with " << k << " non-zero elements: " << brute(nums, k) << endl;
    cout << "Length of longest subarray with " << k << " non-zero elements: " << better(nums, k) << endl;

    return 0;
}