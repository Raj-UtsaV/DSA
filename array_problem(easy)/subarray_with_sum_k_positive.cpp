#include <thread>
#include <chrono>
#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <unordered_map>

using namespace std;

int brute(int arr[], int n, int k)
{
    int maxlen = 0;
    for (int i = 0; i < n; i++)
    {
        int sum = 0;
        for (int j = i; j < n; j++)
        {
            sum += arr[j];
            if (sum == k)
            {
                maxlen = max(maxlen, j - i + 1);
            }
        }
    }
    return maxlen;
}

int better(int arr[], int n, int k)
{
    unordered_map<long, int> prefixsum;
    long sum = 0;
    long maxlen = 0;
    for (int i = 0; i < n; i++)
    {
        sum += arr[i];

        if (sum == k)
            maxlen = max(maxlen, long(i + 1));

        long rem = sum - k;
        if (prefixsum.find(rem) != prefixsum.end())
        {
            maxlen = max(maxlen, long(i) - prefixsum[rem]);
        }

        if (prefixsum.find(sum) == prefixsum.end())
            prefixsum[sum] = i;
    }
    return maxlen;
}

int optimal(int arr[], int n, int k){
    int left=0,right=0,maxlen=0;
    int sum =0;
    while(right<n){
        sum+=arr[right];

        while(sum>k ){
            sum-=arr[left];
            left++;
        }

        if(sum==k){
            maxlen = max(maxlen,right-left+1);
            sum-=arr[left];
            left++;
        }
        right++;
       
    }
    return maxlen;
}

int main()
{
    std::chrono::time_point<std::chrono::high_resolution_clock> starttime;
    {
        system("cls");
        starttime = std::chrono::high_resolution_clock::now();
    }

    // todo In this block write your code
    {
        int n = 7;
        int arr[] = {1,2,3,1,1,1,1};
        int k = 3;

        cout << brute(arr, n, k) << endl;
        cout << better(arr, n, k) << endl;
        cout << optimal(arr, n, k) << endl;
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