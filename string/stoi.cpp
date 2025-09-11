#include <iostream>
using namespace std;

int tointeger(string s)
{
    long long int n = s.length();
    long long int num = 0;
    long long int k = 1;
    long long int i = 0;
    while (s[i] == ' ')
    {
        i++;
    }
    if (s[i] == '-')
    {
        k = -1;
        i++;
    }
    if (s[i] == '+' && k == 1)
        i++;
    while (i < n)
    {
        if (num > INT_MAX)
            break;
        if (s[i] >= '0' && s[i] <= '9')
            num = num * 10 + (s[i] - '0');
        else
            break;
        i++;
    }
    num = num * k;
    if (num <= INT_MIN)
        return INT_MIN;
    else if (num >= INT_MAX)
        return INT_MAX;

    return num;
}

int main()
{
    string s;
    cin >> s;
    cout<<tointeger(s);

    return 0;
}