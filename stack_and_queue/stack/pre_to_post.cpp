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
string post(string s){
    stack<string> res;
    for (int i = s.length(); i >= 0;i--){
        if(isoperator(s[i])){
            string op1 = res.top();
            res.pop();
            string op2 = res.top();
            res.pop();
            res.push(op1 + op2 + s[i]);

        }
        else{
            res.push(string(1, s[i]));
        }
    }
    return res.top();
}

int main(){
    string prefix = "*-A/BC-/AKL";
    cout << "Postfix Expression: " << post(prefix) << endl;
    return 0;
}