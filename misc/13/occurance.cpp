// // #include<iostream>
// // using namespace std;

// // int rightIndex(int arr[],int size,int key){
// //     for(int i=0;i<size;i++){
// //         if(key==arr[i]){
// //             return i;
// //         }
// //     }
// //     return -1;
// // }

// // int ledtIndex(int arr[],int size,int key){
// //     for(int i=size-1;i<size;i--){
// //         if(key==arr[i]){
// //             return i;
// //         }
// //     }
// //     return -1;
// // }

// // int main(){
// //     int arr[5]={1,2,1,2,5};
// //     int key;
// //     //cin>>key;

// //     int c=rightIndex(arr,5,2);
// //     cout<<c<<" ";
// //     int d = ledtIndex(arr,5,2);
// //     cout<<d;

// //     return 0;
// // }

// #include<iostream>
// using namespace std;

// int dirstoccurance(int arr[],int n,int key){
//     int s = 0;
//     int e = n-1;
//     int ans = -1;
//     int mid=s + (e-s)/2;

//     while(s<=e){

//       if(arr[mid] == key){
//         ans = mid;
//         e=mid-1;

//       }

//       else if(arr[mid] < key){ //aage jao
//         s=mid+1;
//       }

//       else if(arr[mid] > key){ //piche jao
//         e=mid-1;
//       }

//       mid=s+(e-s)/2;

//     }
//     return ans;

// }

// //  int lastoccurance(int arr[],int n,int key){
// //     int s = 0;
// //     int e = n-1;
// //     int ans = -1;
// //     int mid=s + (e-s)/2;

// //     while(s<=e){

// //       if(arr[mid] == key){
// //         ans = mid;
// //         e=mid-1;

// //       }

// //       else if(arr[mid] < key){ //piche jao
// //         e=mid-1;
// //       }

// //       else if(arr[mid] > key){ //aage jao
// //         s=mid+1;
// //       }
// //       mid=s+(e-s)/2;

// //     }
// //     return ans;
// // }

// int lastoccurance(int arr[],int n,int key){
//     int s = 0;
//     int e = n-1;
//     int ans = -1;
//     int mid=s + (e-s)/2;

//     while(s<=e){

//       if(arr[mid] == key){
//         ans = mid;
//         s = mid+1;

//       }

//       else if(arr[mid] < key){ //aage jao
//         s=mid+1;
//       }

//       else if(arr[mid] > key){ //piche jao
//         e=mid-1;
//       }

//       mid=s+(e-s)/2;

//     }
//     return ans;

// }

// int main(){
//     int arr[8]={1,2,3,2,1,2,2,1};
//     int key;
//     cin>>key;

//     int c = dirstoccurance(arr,8,key);
//     int d = lastoccurance(arr,8,key);

//     cout<<c<<" "<<d;

//     return 0;

// }

#include <iostream>
using namespace std;

int dirstoccurance(int arr[], int size, int key)
{
  int s = 0;
  int e = size - 1;
  int mid = s + (e - s) / 2;
  int ans = -1;

  while (s <= e)
  {
    if (arr[mid] == key)
    {
      ans = mid;
      e = mid - 1;
    }

    if (arr[mid] < key)
    {
      s = mid + 1;
    }

    if (arr[mid] > key)
    {
      e = mid - 1;
    }

    mid = s + (e - s) / 2;
  }
  return ans;
}

int lastoccurance(int arr[], int size, int key)
{
  int s = 0;
  int e = size - 1;
  int mid = s + (e - s) / 2;
  int ans = -1;

  while (s <= e)
  {
    if (arr[mid] == key)
    {
      ans = mid;
      s = mid + 1;
    }

    if (arr[mid] < key)
    {
      s = mid + 1;
    }

    if (arr[mid] > key)
    {
      e = mid - 1;
    }

    mid = s + (e - s) / 2;
  }
  return ans;
}

int main()
{
  // int a=8;
  // cin>>a;
  int key;
  cin >> key;
  int arr[8] = {0, 0, 1, 1, 2, 2, 2, 2};

  int c = dirstoccurance(arr, 8, key);
  int d = lastoccurance(arr, 8, key);

  cout << c << " " << d;

  return 0;
}