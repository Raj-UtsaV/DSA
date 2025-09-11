#include <iostream>
using namespace std;
 
int main() {
    int arr[5] = {0, 2, 1, 0, 2};
    int s = 0, mid = 0, e = 4;
    while(mid<e){
        if(arr[mid] == 0) {
            swap(arr[s], arr[mid]);
            s++;
            mid++;
        }
        else if(arr[mid] == 1){
            mid++;
        }
        else{
            swap(arr[e], arr[mid]);
            e--;
        }
    }
    for(auto i:arr){
        cout << i << " ";
    }
    return 0;
}