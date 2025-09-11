#include <thread>
#include <chrono>
#include <iostream>
#include <string>

std::string brute(std::string s, std::string t)
{
    int minlen = INT_MAX;
    int startindex = -1;
    int n = s.length();
    int m = t.length();
    for (int i = 0; i < n; i++)
    {
        int hash[256] = {0};
        int count = 0;
        for (int j = 0; j < m; j++)
        {
            hash[t[j]]++;
        }
        for (int j = i; j < n; j++)
        {
            if (hash[s[j]] > 0)
                count++;
            hash[s[j]]--;
            if (count == m)
            {
                if (j - i + 1 < minlen)
                {
                    minlen = j - i + 1;
                    startindex = i;
                    break;
                }
            }
        }
    }
    if (startindex == -1)
        return "";
    return s.substr(startindex, minlen);
}

std::string optimal(std::string s, std::string t)
{
    int n = s.length();
    int m = t.length();
    int left = 0, right = 0, count = 0, minLen = INT_MAX, startindex = -1;
    int hash_t[256] = {0};

    for (int i = 0; i < m; i++)
        hash_t[t[i]]++;

    while(right<n){
        if(hash_t[s[right]] > 0){
            count++;
        }
        hash_t[s[right]]--;
        while(count==m){
            if(right-left+1<minLen){
                minLen = right-left+1;
                startindex = left;
            }
            hash_t[s[left]]++;
            if(hash_t[s[left]]>0){
                count--;
            }
            left++;
        }
        right++;
    }
    if(startindex==-1) return "";
    return s.substr(startindex, minLen);
}

int main()
{
    {
        system("cls");
    }

    //! In this block write your code
    {
        std::string s = "ADOBECODEBANC";
        std::string t = "ABC";
        std::cout << brute(s, t) << std::endl; // output "BANC"
        std::cout << optimal(s, t) << std::endl; // output "BANC"
    }

    {
        std::this_thread::sleep_for(std::chrono::seconds(4));
        system("cls");
    }
    return 0;
}