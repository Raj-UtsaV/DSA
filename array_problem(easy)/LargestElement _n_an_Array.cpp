#include <iostream>
using namespace std;
 
int main() {
    int arr[5] = {1, 3, 2, 4, 5};
    int x = arr[0];
    for (int i = 1; i < 5;i++){
        if(x<arr[i])
            x = arr[i];
    }
    cout << x;
    return 0;
}