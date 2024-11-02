#include <iostream>
#include<string>
#include<vector>

using namespace std;

void solve(string digit,string output,long long unsigned int index,vector<string>& ans,string mapping[]){
    if(index >= digit.length()){
        ans.push_back(output);
        return;
    }

    int number = digit[index] - '0';
    string value = mapping[number];

    for (long long unsigned int i = 0; i < value.length();i++){
        output.push_back(value[i]);
        solve(digit, output, index + 1, ans, mapping);
        output.pop_back();
    }
    
    
}
 
int main() {
    string digit = "23";
    vector<string> ans;
    string output = "";
    string mapping[10] = {"", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"};
    int index = 0;
    solve(digit, output, index, ans, mapping);

    for(auto i:ans){
        cout << i  << " ";
    }

    return 0;
}