#include <thread>
#include <chrono>
#include <iostream>
#include <vector>
#include <unordered_map>

int brute(std::vector<int> &nums, int k)
{
    int maxsubarr = 0;
    int n = nums.size();
    for (int i = 0; i < n; i++)
    {
        std::unordered_map<int, int> mpp;
        for (int j = i; j < n; j++)
        {
            mpp[nums[j]]++;
            if (mpp.size() > k)
                break;
            if (mpp.size() == k)
                maxsubarr++;
        }
    }
    return maxsubarr;
}

int subarrlessequalk(std::vector<int> &nums, int k)
{
    int maxsubarr = 0, left = 0, right = 0, n = nums.size();
    std::unordered_map<int, int> mpp;
    while (right < n)
    {
        mpp[nums[right]]++;
        while (mpp.size() > k)
        {
            mpp[nums[left]]--;
            if(mpp[nums[left]]==0) mpp.erase(nums[left]);
            left++;
        }
        maxsubarr += right - left+1 ;
        right++;
    }
    return maxsubarr;
}

int main()
{
    {
        system("cls");
    }

    //! In this block write your code
    {
        std::vector<int> nums = {1,2,1,3,4};
        int k = 3;
        std::cout << brute(nums, k) << std::endl;  // output 3
        std::cout << subarrlessequalk(nums, k)-subarrlessequalk(nums,k-1) << std::endl;  // output 3
    }

    {
        std::this_thread::sleep_for(std::chrono::seconds(4));
        system("cls");
    }
    return 0;
}