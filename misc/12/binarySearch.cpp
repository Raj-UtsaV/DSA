#include<iostream>
using namespace std;

int search(int arr[],int size,int key){
    int start = 0;
    int end = size-1;

    //int mid = (start + end)/2; ......not work if srart and end value is very big and their addition goes beyoend int limit...
    int mid = start + (end - start)/2;

    while(start <= end){
         
        if(arr[mid]==key){
            return mid;
        }

        if(key > arr[mid]){
            start=mid+1;
        }

        if( key < arr[mid]){
            end=mid-1;
        }

        mid = start + (end - start) / 2;
    }
    return -1;
}

int main(){
    int arr[5]={3,5,9,13,27};
    int key;
    cin>>key;

    int index = search(arr,6,key);

    cout<<index;

    return 0;
}