#include <iostream>
#include <string>

using namespace std;

char maxoccur(string s)
{

    int arr[26] = {0};
    for (int i = 0; i < s.length(); i++)
    {

        char ch = s[i];
        int num = 0;
        if (ch >= 'a' && ch <= 'z')
        {
            num = ch - 'a';
        }
        else
        {
            num = ch - 'A';
        }
        arr[num]++;
    }

    int maxi = 0,ans = 0;
    for(int i = 0; i < 26; i++)
    {
        if(maxi < arr[i]){
            ans = i;
            maxi = arr[i];
        }
    }

    return  ('a'+ans);
}

int main()
{
    string s;
    cin >> s;
    cout << maxoccur(s);
    return 0;
}