//! basic idea
//? infix operand + operator + operator
//? postfix operand + operand + operator
//? prefix operator + operand + operand

#include<iostream>
#include<stack>
#include<string>

using namespace std;

bool isOperator(char c)
{
    return (c == '+' || c == '-' || c == '*' || c == '/' || c == '^');
}

string infix(string s) {
    stack<string> res;
    for (int i = 0;i<s.length();i++) {
        if(isOperator(s[i])){
            string op1 = res.top();
            res.pop();
            string op2 = res.top();
            res.pop();
            string temp = "(" + op2 + s[i] + op1 + ")";
            res.push(temp);
        }
        else{
            res.push(string(1, s[i]));
        }
    }
    return res.top();
}

int main(){
    string postfix = "ab*c+";
    cout << "Infix expression: " << infix(postfix) << endl;
    return 0;
}