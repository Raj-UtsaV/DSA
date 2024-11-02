#include <iostream>
using namespace std;
 
int main() {
    int arr[5] = {1, 4, 2, 4, 5};
    

    //todo better approach
    // int largest = INT_MIN;
    // for (int i = 0; i < 5;i++){
    //     if(arr[i]>largest)
    //         largest = arr[i];
    // }

    // int slargest = INT_MIN;
    // for (int i = 0; i < 5;i++){
    //     if((slargest < arr[i]) && (arr[i] < largest)){
    //         slargest = arr[i];
            
    //     }
    // }
    // cout << slargest;

    //todo best
    int largest = arr[0];
    int slargest = INT_MIN;
    for (int i = 1; i < 5;i++){
        if(arr[i]>largest){
            slargest = largest;
            largest = arr[i];
        }
        else if(arr[i] <largest && arr[i] > slargest){
            slargest = arr[i];
        }
    }
    cout << slargest;

    return 0;
}