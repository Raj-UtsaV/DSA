#include <iostream>
using namespace std;

int check(int arr[],int n){
    for (int i = 1; i < n;i++){
        if(arr[i]<arr[i-1])
            return 0;
    }
    return 1;
}
 
int main() {
    int arr[5] = {1,2,3,5,5};
    cout << check(arr,5);
    return 0;
}