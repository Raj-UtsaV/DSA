#include <iostream>
#include <thread>
#include <chrono>
#include <vector>
#include <unordered_map>

using namespace std;

int brute(vector<int> nums, int goal)
{
    int maxsubarr = 0;
    int n = nums.size();
    for (int i = 0; i < n; i++)
    {
        int sum = 0;
        for (int j = i; j < n; j++)
        {

            sum += nums[j];
            if (sum == goal)
            {
                maxsubarr++;
            }
            if (sum > goal)
                break;
        }
    }
    return maxsubarr;
}

int better(vector<int> nums, int goal)
{

    int n = nums.size();
    unordered_map<int, int> mpp;
    int preSum = 0, cnt = 0;

    mpp[0] = 1;
    for (int i = 0; i < n; i++)
    {

        preSum += nums[i];

        int remove = preSum - goal;

        cnt += mpp[remove];

        mpp[preSum] += 1;
    }
    return cnt;
}

int subarrlessequalgoal(vector<int> nums, int goal)
{
    int left = 0, right = 0,count = 0,sum=0;
    if(goal < 0) return left;
    while(right<nums.size()){
        sum+=nums[right];
        while(sum>goal){
            sum-=nums[left];
            left++;
        }
        count += right-left+1;
        right++;
    }
    return count;

}

int main()
{
    {
        system("cls");
    }

    //! In this block write your code
    {
        vector<int> nums = {0,0,0,0,0};
        int goal = 0;
        cout << brute(nums, goal) << endl;
        cout << better(nums, goal) << endl;    // output 4
        cout << subarrlessequalgoal(nums, goal) - subarrlessequalgoal(nums,goal-1) << endl; // output 4
    }

    {
        this_thread::sleep_for(chrono::seconds(4));
        system("cls");
    }
    return 0;
}