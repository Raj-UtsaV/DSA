#include <thread>
#include <chrono>
#include <iostream>
#include <numeric>
#include <string>
#include <algorithm>
#include <unordered_map>

int brute(std::string s, int k)
{
    int n = s.length();
    int maxlen = 0;
    for (int i = 0; i < n; i++)
    {
        int arr[26] = {0};
        for (int j = i; j < n; j++)
        {
            arr[s[j] - 'a'] = 1;
            if (std::accumulate(arr, arr + 26, 0) > k)
                break;
            maxlen = std::max(maxlen, j - i + 1);
        }
    }
    return maxlen;
}

int brute1(std::string s, int k)
{
    int maxlen = 0;
    std::unordered_map<char, int> mpp;
    int n = s.length();
    for (int i = 0; i < n; i++)
    {
        mpp.clear();
        for (int j = i; j < n; j++)
        {
            mpp[s[j]]++;
            if (mpp.size() > k)
                break;
            maxlen = std::max(maxlen, j - i + 1);
        }
    }
    return maxlen;
}

int better(std::string s, int k)
{
    int maxlen = 0, left = 0, right = 0, n = s.length();
    std::unordered_map<char, int> mpp;
    while (right < n)
    {
        mpp[s[right]]++;
        while (mpp.size() > k)
        {
            mpp[s[left]]--;
            if (mpp[s[left]] == 0)
                mpp.erase(s[left]);
            left++;
        }
        maxlen = std::max(maxlen, right - left + 1);
        right++;
    }
    return maxlen;
}

int optimal(std::string s, int k)
{
    int maxlen = 0, left = 0, right = 0, n = s.length();
    std::unordered_map<char, int> mpp;
    while (right < n)
    {
        mpp[s[right]]++;
        if (mpp.size() > k)
        {
            mpp[s[left]]--;
            if (mpp[s[left]] == 0)
                mpp.erase(s[left]);
            left++;
        }
        if (mpp.size() <= k)
            maxlen = std::max(maxlen, right - left + 1);
        right++;
    }
    return maxlen;
}

int main()
{
    {
        system("cls");
    }

    //? In this block write your code
    {
        std::string s = "abbbbbbc";
        int k = 2;
        std::cout << brute(s, k) << std::endl;   // output 7
        std::cout << brute1(s, k) << std::endl;  // output 7
        std::cout << better(s, k) << std::endl;  // output 7
        std::cout << optimal(s, k) << std::endl; // output 7
    }

    {
        std::this_thread::sleep_for(std::chrono::seconds(5));
        system("cls");
    }
    return 0;
}