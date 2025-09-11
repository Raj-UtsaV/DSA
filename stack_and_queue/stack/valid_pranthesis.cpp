#include <iostream>
#include<stack>
using namespace std;

bool valid(string s){
    stack<char> st;
    for (int i = 0;i<s.length();i++){
        if(s[i] == '(' || s[i] == '{' || s[i] == '['){
            st.push(s[i]);
        }
        else {
            if(!st.size())
                return 0;
            char c = st.top();
            if( c == '{' && s[i] == '}' ){
                    st.pop();
            }
            else if( c == '(' && s[i] == ')' ){
                    st.pop();
            }
            else if( c == '[' && s[i] == ']' ){
                    st.pop();
            }
            else
                return 0;
        }
    }
    if(st.size())
        return 0;
    return 1;
}
 
int main() {
    string s = "(])";
    cout << valid(s);
    return 0;
}