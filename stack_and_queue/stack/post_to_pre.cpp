//! basic idea
//? infix operand + operator + operator
//? postfix operand + operand + operator
//? prefix operator + operand + operand

#include<iostream>
#include<stack>
using namespace std;

bool isoperator(char c)
{
    return (c == '+' || c == '-' || c == '*' || c == '/' || c == '^');
}

string pre(string s){
    stack<string> res;
    for (int i = 0;i<s.length();i++)
    {
        if(isoperator(s[i])){
            string op1 = res.top();
            res.pop();
            string op2 = res.top();
            res.pop();
            res.push(s[i]+op2+op1);
        }
        else
            res.push(string(1, s[i]));
    }
    return res.top();
}

int main(){
    string postfix = "ABC/-AK/L-*";
    cout << "Prefix expression: " << pre(postfix) << endl;
    return 0;
}