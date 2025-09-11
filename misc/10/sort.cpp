#include<iostream>
using namespace std;

void printArray(int arr[],int size){
     for(int i=0 ;i<size;i++){
            cout<<arr[i]<<" ";
        }
        cout<<endl;
}


void sort(int arr[],int n){
    int left=0,middle=(n-1)/2,right=n-1;
    
    while(arr[left]==0 && left<middle){
        left++;
    }

    while(arr[middle]==1 && middle<right){
        middle++;
    }

    while(arr[right]==2 && (middle+2)<right){
        right--;
    }

    if((left==1 || left ==2)&& middle==0 && left<middle){
        swap(arr[left],arr[middle]);
    }

    if((left==1 || left ==2)&& right==0 && left<middle){
        swap(arr[left],arr[right]);
    }
    if(middle ==2  && right==1 && middle<right ){
        swap(arr[middle],arr[right]);
    }
    
    
}

int main(){
    int  arr[9]={0,1,2,1,2,0,2,1,0};
    sort(arr,9);
    printArray(arr,9);
    return 0;
}