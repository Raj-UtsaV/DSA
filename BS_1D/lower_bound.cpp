///? lower bound smallest index where arr[index]>=k 
//? uppper bound smallest index where arr[index]>k

// todo STL lower_bound(arr.begin(),arr.end(),k) - arr.begin();
// todo STL upper_bound(arr.begin(),arr.end(),k) - arr.begin();

#include <iostream>
using namespace std;

int lower_bound(int arr[],int n,int k){
    int s = 0;
    int e = n - 1;
    int ans = n;
    while(s<=e){
        int mid = s + (e - s) / 2;
        if(arr[mid] >= k){
            ans = mid;
            e = mid - 1;
        }
        else
            s = mid + 1;
    }
    return arr[ans];
}

int upper_bound(int arr[],int n,int k){
    int s = 0;
    int e = n - 1;
    int ans = n;
    while(s<=e){
        int mid = s + (e - s) / 2;
        if(arr[mid] > k){
            ans = mid;
            e = mid - 1;
        }
        else
            s = mid + 1;
    }
    return arr[ans];
}

 
int main() {
    int arr[5] = {1, 2, 3, 4, 6};
    cout << lower_bound(arr, 5, 4)<<" ";
    cout << upper_bound(arr, 5, 4);
    return 0;
}