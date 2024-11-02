#include <iostream>
#include<string>

using namespace std;

bool checkEqual(int cnt1[26],int cnt2[26]){
    for(int i=0;i<26;i++){
        if(cnt1[i] != cnt2[i]) return 0;
    }
    return 1;
}

string found(string s1,string s2){
    //! character count array
    int cnt1[26] = {0};

    for(int i =0;i<s1.length();i++){
        int index = s1[i] - 'a';
        cnt1[index]++;
    }

    //* now traverse s2 string  and check if all characters of s1 are present in window of s1 string length
    int i = 0;
    int windowSize = s1.length();
    int cnt2[26] = {0};

    //!running for first window
    while(i< windowSize && i<s2.length()){
        int index = s2[i] - 'a';
        cnt2[index]++;
        i++;
    }

    if(checkEqual(cnt1,cnt2)) return "yes";

    //!aage window process kro
    while(i < s2.length()){
        char newChar = s2[i];
        int index = newChar - 'a';
        cnt2[index]++;

        char oldChar = s2[i-windowSize];
        index = oldChar - 'a';
        cnt2[index]--;

        i++;
        if(checkEqual(cnt1,cnt2)) return "yes";
    }
    return "no";

}
 
int main() {
    string s1,s2;
    cin>>s1>>s2;
    cout<<found(s1,s2)<<endl;
  return 0;
}