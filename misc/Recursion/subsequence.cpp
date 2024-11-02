#include <iostream>
#include<vector>
#define llu long long unsigned
using namespace std;

void solve(string str, string output, llu int index, vector<string> &ans)
{

    // todo Base case
    if (index >= str.size())
    {
        ans.push_back(output);
        return;
    }

    // todo Exclude
    solve(str, output, index + 1, ans);

    // todo Include
    char element = str[index];
    output.push_back(element);
    solve(str, output, index + 1, ans);
}

int main()
{
    string str = "abc";
    vector<string> ans;
    string output = "";
    llu int index = 0;
    solve(str, output, index, ans);

    for(auto i:ans){
        cout << i << " ";
    }

    
    return 0;
}