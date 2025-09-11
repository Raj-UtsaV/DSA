#include <iostream>
#include<math.h>
using namespace std;

int koko_banana_brute(int *arr, int n, int h)
{
    int s = 1;
    while (true)
    {
        int cnt = 0;
        for (int i = 0; i < n; i++)
        {
            cnt += ceil((double)(arr[i]) / (double)(s));
        }
        if (cnt > h)
        {
            s++;
            continue;
        }
        if(cnt<=h){
            return s;
            break;
        }
        else
            cnt = 0;
    }
    return -1;
}

int koko_banana_optimal(int *arr,int n,int h){
    int maxi = INT_MIN;
    for(int i=0;i<n;i++){
        maxi = max(arr[i], maxi);
    }
    int low = 1, high = maxi;
    while(low<=high){
        int mid = low + (high - low) / 2;
        int cnt = 0;
        for(int i=0;i<n;i++){
            cnt += ceil((double)arr[i] / (double)mid);
        }
        if(cnt<=h){
            high = mid - 1;
        }
        else
            low = mid + 1;
    }
    return low;
}

int main()
{
    int arr[] = {3, 6, 7, 11};
    int h = 8;
    int n = sizeof(arr) / sizeof(arr[0]);
    cout<<koko_banana_brute(arr, n, h)<<endl;
    cout<<koko_banana_optimal(arr, n, h)<<endl;

    return 0;
}