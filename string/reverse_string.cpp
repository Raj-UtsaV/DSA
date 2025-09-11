#include <iostream>
#include<map>
#include <string>
#define llu long long unsigned int
using namespace std;

bool reverse(string s, string t)
{
    llu cnt = 1;
    llu cnt1 = 1;
    for (llu i = 1; i < s.length();i++){
        if(s[i] != s[i-1])
            cnt++;
        if(t[i]!=t[i-1])
            cnt1++;
    }

        map<char, char> mpp;
    for (llu i = 0; i < s.length(); i++){
        mpp[s[i]] = t[i];
    }
    cout << cnt << " " << mpp.size();
    if(cnt1 != cnt)
         return false;
    if(mpp.size() == cnt)
        return true;
    else
        return false;
}

int main()
{
    string s;
    cin >> s;
    string t;
    cin >> t;
    cout<<reverse(s, t);
    return 0;
}