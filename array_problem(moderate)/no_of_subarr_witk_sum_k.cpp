#include <thread>
#include <chrono>
#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <unordered_map>

using namespace std;

int brute(vector<int> nums, int k)
{
    int count = 0;
    for (int i = 0; i < nums.size(); i++)
    {
        int sum = 0;
        for (int j = i; j < nums.size(); j++)
        {
            sum += nums[j];
            if (sum == k)
                count++;
        }
    }
    return count;
}

int optmized(vector<int> nums, int k)
{
    int n = nums.size();
    unordered_map<int, int> mpp;
    int preSum = 0, cnt = 0;

    mpp[0] = 1;
    for (int i = 0; i < n; i++)
    {

        preSum += nums[i];

        int remove = preSum - k;

        cnt += mpp[remove];

        mpp[preSum] += 1;
    }
    return cnt;
}

int main()
{
    std::chrono::time_point<std::chrono::high_resolution_clock> starttime;
    {
        system("cls");
        starttime = std::chrono::high_resolution_clock::now();
    }

    // todo:-> In this block write your code
    {
        vector<int> nums = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
        int k = 15;
        cout << "Brute Force: " << brute(nums, k) << endl;  // output 3
        cout << "Optimized: " << optmized(nums, k) << endl; // output 3
    }

    {
        auto endtime = std::chrono::high_resolution_clock::now();
        auto duration = std::chrono::duration_cast<std::chrono::microseconds>(endtime - starttime).count();
        std::cout << std::endl;
        std::cout << "Execution time: " << duration / 1000000.0 << " seconds" << std::endl;
        std::this_thread::sleep_for(std::chrono::seconds(4));
        system("cls");
    }
    return 0;
}