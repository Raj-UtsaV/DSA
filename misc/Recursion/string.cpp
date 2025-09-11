#include <iostream>
#include <string>
using namespace std;

string reverse(int i, int j, string s)
{
    if (i > j)
        return s;

    swap(s[i], s[j]);
    i++;
    j--;
    return reverse(i, j, s);
}

void reverse1(int i, string &s)
{

    if (i > s.length() - 1 - i)
        return;

    swap(s[i], s[s.length() - 1 - i]);
    i++;
    reverse1(i, s);
}

string isPallindrome(string &s, int i = 0)
{
    if (i > s.length() - 1 - i)
        return "Pallindrome";

    if (s[i] != s[s.length() - 1 - i])
        return "Not Pallindrome";

    else
    {
        i++;
        return isPallindrome(s, i);
    }
}

/*
void reverse2 (string s,int k){
    if(k<=0)
        return;

    reverse2(s + 1, k - 1);
    cout << s;
}
*/

int main()
{
    string s = "abcde";
    string s1 = "utsav";
    string s3 = "abccba";

    cout << reverse(0, s.length() - 1, s1) << endl;
    reverse1(0, s);
    cout << s << endl;
    // reverse2(s, s.length() - 1); //? not work because in string whole string send at a time not first letter

    if (s3 == reverse(0, s3.length() - 1, s3))
        cout << "pallindrome" << endl;
    else
        cout << "Not a pallindrome" << endl;

    cout << isPallindrome(s3);

    
    return 0;
}