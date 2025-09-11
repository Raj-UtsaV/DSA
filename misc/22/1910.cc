#include <iostream>
#include<string>
using namespace std;
 

string found(string s,string part){
    while(s.length()!=0 && s.find(part) <s.length()){
        s.erase(s.find(part),part.length());
    }
    return s;
}
int main() {
    string s,part;
    cin>>s>>part;
    cout<<found(s,part);
  return 0;
}