#include <iostream>
#include <chrono>
#include <thread>
#include <string>
#include <algorithm>
using namespace std;

int brute(string s, int k)
{
    int maxlen = 0;
    int n = s.length();
    for (int i = 0; i < n; i++)
    {
        int hash[26];
        fill(hash, hash + 26, 0);
        int maxfreq = 0;
        for (int j = i; j < n; j++)
        {
            hash[s[j] - 'A']++;
            maxfreq = max(maxfreq, hash[s[j] - 'A']);
            int change = (j - i + 1) - maxfreq;
            if (change <= k)
                maxlen = max(maxlen, j - i + 1);
            else
                break;
        }
    }
    return maxlen;
}

int better(string s, int k)
{
    int maxlen = 0,left=0,right=0,maxfreq=0,n=s.length();
    int hash[26] = {0};
    while(right<n){
        hash[s[right] - 'A']++;
        maxfreq = max(maxfreq, hash[s[right] - 'A']);
        while(right-left+1-maxfreq > k){
            hash[s[left] - 'A']--;
            left++;
            maxfreq = *max_element(hash, hash+26); //finding the maxfreq
        }
        maxlen = max(maxlen, right - left + 1);
        right++;
    }
    return maxlen;
}


int optimal(string s, int k){
    int maxfreq = 0, maxlen = 0, left =0, right = 0, n = s.length();
    int hash[26] = {0};
    while(right < n){
        hash[s[right] - 'A']++;
        maxfreq = max(maxfreq, hash[s[right] - 'A']);
        if (right - left + 1 - maxfreq > k)
        {
            hash[s[left] - 'A']--;
            left++;
        }
        maxlen = max(maxlen, right - left + 1);
        right++;
    }
    return maxlen;

}

int main()
{
    {
        system("cls");
    }

    //! in this block write your code
    {
        string s = "ABBB";
        int k = 2;
        cout << brute(s, k) << endl; // output 4
        cout << better(s, k) << endl;
        cout << optimal(s, k) << endl; // output 4
    }

    {
        this_thread::sleep_for(chrono::seconds(4));
        system("cls");
    }
    return 0;
}
