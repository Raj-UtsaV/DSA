// #include <iostream>
// using namespace std;

// int pivot(int nums[], int size)
// {
//     int s = 0;
//     int e = size - 1;
//     int mid =  (e ) / 2;
//     int sum = 0;
//     int add = 0;
//     while (mid<e)
//     {
//         for (int i = 0; i <= mid; i++)
//         {
//             sum = sum + nums[i];
//         }
//         for (int j = mid; j <= e; j++)
//         {
//             add = add + nums[j];
//         }
//         if (sum == add)
//         {
//             return mid;
//         }
//         else if (sum < add)
//         {
//             mid = mid + 1;
//         }
//         else
//         {
//             mid = mid - 1;
//         }
//          sum=0;
//          add=0;
        
//     }
//     return -1;
// }

// int main()
// {
//     int nums[6] = {-1, -1, -1, -1, -1, -1};
//     cout << pivot(nums, 6);
//     return 0;
// }


#include<iostream>
#include<vector>
using namespace std;

int pivot(vector<int>&arr,int size){


int s = 0;
int e = size - 1;
int mid = s + (e - s) / 2;



while(s<e){
    if(arr[mid]>=arr[0]){
        s=mid+1;
    }
    else{
        e=mid;
    }
    mid=s+(e-s)/2;
}
 return s;
}

int main(){
    vector<int> arr = {2, 1};
    cout<<pivot(arr,arr.size());
    return 0;
}