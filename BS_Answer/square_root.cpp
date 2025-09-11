#include <iostream>
using namespace std;

int square_root(int x){
    int s = 0;
    int e = x / 2;
    long long int mid = s + (e - s) / 2;
    long long val = 1;
    while(s<=e){
        mid = s + (e - s) / 2;
        if(mid*mid<=x){
            val = mid;
            s = mid + 1;
        }
        else
            e = mid - 1;
        
    }
    return val;
}
 
int main() {
    int x;
    cin >> x;
    cout << square_root(x);
    return 0;
}