//! basic idea
//? infix operand + operator + operator
//? postfix operand + operand + operator
//? prefix operator + operand + operand

#include<iostream>
#include<stack>
using namespace std;

bool isoperator(char c){
    return (c=='+' || c=='-' || c=='*' || c=='/' || c=='^');
}

string convert(string s){
    stack<string> res;
    for (int i=s.size() - 1; i >= 0;i--){
        if(isoperator(s[i])){
            string op1 = res.top(); res.pop();
            string op2 = res.top(); res.pop();
            string temp = "(" + op1 + s[i] + op2 + ")";
            res.push(temp);
        }
        else{
            res.push(string(1, s[i]));
        }
    }
    return res.top();
}

int main(){
    string s = "*-A/BC-/AKL";
    cout << "Infix expression: " << s << endl;
    cout << "Prefix expression: " << convert(s) << endl;
    return 0;
}