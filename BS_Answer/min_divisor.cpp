#include <iostream>
#include<algorithm>
#include<math.h>
using namespace std;

int min_divisor(int *arr,int n,int l){
    int s = 1;
    int e = *max_element(arr,arr+n);

    while(s<=e){
        int cnt = 0;
        int mid = s + (e - s) / 2;
        
        for (int i = 0; i < n;i++){
            cnt += ceil((double)arr[i] / (double)mid);
        }
        if(cnt<=l){
            e = mid - 1;
        }
        else
            s = mid + 1;
    }
    return s;
}
 
int main() {
    int arr[] = {1,9,5,2};
    int n = sizeof(arr)/sizeof(arr[0]);
    int limit = 6;
    cout<<  min_divisor(arr, n, limit);
    
    return 0;
}

