#include <iostream>
#include <thread>
#include <chrono>
#include<vector>
using namespace std;

int brute(vector<int> &nums,int k){
    int maxsubarr=0;
    int n = nums.size();
    for (int i = 0; i < n; i++){
        int cntodd=0;
        for(int j=i;j<n;j++){
            if(nums[j]%2 != 0 ) cntodd++;
            if(cntodd==k) maxsubarr++;
            else if(cntodd >k) break;
        }
    }
    return maxsubarr;
}

int optimal(const vector<int>& nums, int k) {
    int maxsubarr = 0, left = 0, count = 0;
    for (int right = 0; right < nums.size(); right++) {
        if (nums[right] % 2 != 0)
            k--;
        while (k < 0) {
            if (nums[left] % 2 != 0)
                k++;
            left++;
        }
        maxsubarr += right - left + 1;
    }
    return  maxsubarr;
}

int main() {
   {
        system("cls");
   }
 
   //! In this block write your code
   {
        vector<int> nums = {1,1,2,1,1};
        int k = 3;
        cout << "Brute Force: " << brute(nums, k) << endl; // output 2
        cout << "Optimized: " << optimal(nums, k) << endl; // output 2
   }
 
   {
        this_thread::sleep_for(chrono::seconds(4));
        system("cls");
   }
    return 0;
}