#include <iostream>
#include<math.h>
using namespace std;

int exponential(int a,int b){
    if(b == 0)
        return 1;

    if(b==1)
        return a;

    
    if(b%2 != 0){
        return a * exponential(a, (b / 2)) * exponential(a, (b / 2));
    }
    return exponential(a, (b / 2)) * exponential(a, (b / 2));
}
 
int main() {
    int a, b;
    cout << "Enter a & b : ";
    cin >> a >> b;
    cout << exponential(a, b);
    return 0;
}