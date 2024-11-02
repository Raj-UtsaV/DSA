//! basic idea
//? infix operand + operator + operator
//? postfix operand + operand + operator
//? prefix operator + operand + operand

#include <iostream>
#include <stack>
#define llu long long unsigned
using namespace std;

int prec(char c)
{
    if (c == '^')
        return 3;
    else if (c == '/' || c == '*')
        return 2;
    else if (c == '+' || c == '-')
        return 1;
    else
        return -1;
}

string conversion(string s)
{
    stack<char> st;
    string res;
    for (llu i = 0; i < s.length(); i++)
    {
        if ((s[i] >= '0' && s[i] <= '9') || (s[i] >= 'A' && s[i] <= 'Z') || (s[i] >= 'a' && s[i] <= 'z'))
        {
            res += s[i];
        }

        else if (s[i] == '(')
        {
            st.push('(');
        }

        else if (s[i] == ')')
        {
            while (!st.empty() && st.top() != '(')
            {
                res += st.top();
                st.pop();
            }
            st.pop();
        }

        else
        {
            while (!st.empty() && prec(s[i]) <= prec(st.top()))
            {
                res += st.top();
                st.pop();
            }
            st.push(s[i]);
        }
    }
    while(!st.empty()){
        res += st.top();
        st.pop();
    }
    return res;
}
int main()
{
    string infix = "A*(B+C)/D";
    string postfix = conversion(infix);
    cout << "Postfix expression: " << postfix << endl;
    return 0;
}