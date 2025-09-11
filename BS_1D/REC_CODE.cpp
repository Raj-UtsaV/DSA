#include <iostream>
using namespace std;
 
void rec_code(int arr[],int end,int k,int s=0){
    if(s>end){
        cout << "no";
        return;
    }

    int mid = s + (end - s) / 2;
    if(arr[mid] == k){
        cout << "YES";
        return;
    }
    else if(arr[mid]>k){
        rec_code(arr, mid - 1, k, s);
    }
    rec_code(arr, end, k, mid + 1);
}

int main() {
    int arr[5] = {1, 2, 3, 4, 5};
    rec_code(arr, 5, 6);
    return 0;
}