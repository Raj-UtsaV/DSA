#include <iostream>
using namespace std;

inline getmax(int& a,int& b){
    return (a > b) ? a : b;
}
 
int main() {
    int a = 5, b = 10;
    int ans;

    ans = getmax(a, b);
    cout << ans << endl;

    return 0;
}