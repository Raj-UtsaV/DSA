#include <iostream>
using namespace std;
 
int main() {
    char name[10];
    cin>>name;
    name[3] = '\0';
    cout<<name;
  return 0;
}