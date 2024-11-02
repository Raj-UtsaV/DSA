#include<iostream>
using namespace std;

int peak(int arr[],int size){
    int s=0;
    int e=size-1;
    int mid=s+(e-s)/2;


    while(s<e){
      
        if((arr[mid]>arr[mid+1] )&& (arr[mid]>arr[mid-1])){
            return mid;
           
        }
        if((arr[mid]>arr[mid-1]) ){
            s=mid+1;
        }
        if((arr[mid-1]>arr[mid]) ){
            e=mid; //mid because if the peak element is the value and we use mid-1 the index goes bedore the answer index
        }
        mid=s+(e-s)/2;
    }
   return  mid;
}

int main(){
    int arr[5] = {1,2,3,4,5};
    int k=peak(arr, 5);
    cout<<k;
    return 0;
}