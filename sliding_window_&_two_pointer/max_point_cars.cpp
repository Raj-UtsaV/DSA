#include <thread>
#include <chrono>
#include <iostream>
#include <vector>
#include <numeric>
#include <algorithm>

int optimal(std::vector<int> &nums, int k)
{
    int leftsum = 0,rightsum=0,maxsum=0,rightindex = nums.size()-1;
    leftsum = maxsum = std::accumulate(nums.begin(),nums.begin()+k,0);
    if(k==nums.size()) return leftsum;

    for(int i = k-1;i>=0;i--){
        leftsum -= nums[i];
        rightsum += nums[rightindex];
        maxsum = std::max(maxsum, leftsum + rightsum);
        rightindex--;
    }
    return maxsum;
}

int better(std::vector<int> &nums, int k)
{


    if (k == nums.size())
        return std::accumulate(nums.begin(), nums.end(), 0);

    int n = nums.size();
    std::vector<int> prefix_sum(n + 1, 0);


    for (int i = 0; i < n; ++i)
    {
        prefix_sum[i + 1] = prefix_sum[i] + nums[i];
    }

    int max_points = 0;

    for (int i = 0; i <= k; ++i)
    {
        int left_sum = prefix_sum[i];
        int right_sum = prefix_sum[n] - prefix_sum[n - (k - i)];
        max_points = std::max(max_points, left_sum + right_sum);
    }

    return max_points;
}

int main()
{
    {
        system("cls");
    }

    //! In this block write your code
    {
        std::vector<int> nums = {11, 49, 100, 20, 86, 29, 72};
        int k = 4;
        std::cout << better(nums, k) << std::endl;   // output 232
        std::cout << optimal(nums, k) << std::endl; // output 232
    }

    {
        std::this_thread::sleep_for(std::chrono::seconds(4));
        system("cls");
    }
    return 0;
}