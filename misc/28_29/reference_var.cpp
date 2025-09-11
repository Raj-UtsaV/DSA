#include <iostream>
using namespace std;


void update2(int& n ){
    n++;
}

void update1(int n){
    n++;
}
 
int main() {
    int i = 5;
    
    //?creating ref variable

    int &j = i;

    cout << i << endl;
    cout << j << endl;

    int x = 5;
    cout << "Before : " << x << endl;
    update1(x);
    cout << "After pass by value : " << x << endl;
    update2(x);
    cout << "After pass by reference : " << x << endl;

    return 0;
}