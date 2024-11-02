#include <iostream>
#include <stack>
using namespace std;

string optimal(string s, int k)
{
    string result = "\0";
    int count = 0;
    stack<char> st;
    for (int i = 0; i < s.size(); i++)
    {
        char x = s[i];
        while (!st.empty() && st.top() >= x && count != k)
        {
            st.pop();
            count++;
        }
        st.push(x);
    }

    if (count != k)
    {
        while (count != k)
        {
            st.pop();
            count++;
        }
    }

    while (!st.empty())
    {

        result.insert(result.begin(), st.top());
        st.pop();
    }
    
    while (result[0] == '0')
    {
        result.erase(0, 1);
    }
    return result;
}

int main()
{
    string s = "1242219";
    s = optimal(s, 3);
    cout << s;
    return 0;
}