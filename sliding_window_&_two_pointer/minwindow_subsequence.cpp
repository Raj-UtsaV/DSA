#include <thread>
#include <chrono>
#include <iostream>
#include <string>

std::string brute(std::string s, std::string t)
{
    int minlen = INT_MAX;
    int startindex = -1;
    int n = s.length();
    int k = 0;
    for (int i = 0; i < n; i++)
    {
        if (s[i] == t[0])
        {
            for (int j = i; j < n; j++)
            {
                if (s[j] == t[k])
                    k++;
                if (k == t.length())
                {
                    if (j - i + 1 < minlen)
                    {
                        startindex = i;
                        minlen = j - i + 1;
                    }
                    break;
                }
            }
        }
        k = 0;
    }
    if (startindex == -1)
        return "";
    return s.substr(startindex, minlen);
}

int main()
{
    {
        system("cls");
    }

    //! In this block write your code
    {
        std::string s = "geeksforgeekf";
        std::string t = "eksrg";
        std::cout << brute(s, t) << std::endl;
    }

    {
        std::this_thread::sleep_for(std::chrono::seconds(4));
        system("cls");
    }
    return 0;
}