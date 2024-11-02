#include<iostream>
using namespace std;
void repeat(int arr[],int size){
    int k;
    for(int j=0;j<size;j++){
        k=arr[j];
    
    int ans=0;
    for(int i=0;i<size;i++){
        if(k==arr[i])
        {
            ans=ans+1;
        }
        
    }
    if(ans==2){
        cout<<k;
    }
    }
}

int main(){
    int arr[5]={1,5,3,4,5};
    repeat(arr,5);
    return 0;
}


// #include<iostream>
// using namespace std;

// void repeat(int arr[],int size){
//     int ans=0;
//     for(int i=0;i<size;i++){
//         ans = ans^arr[i];
//     }
//     cout<<ans<<endl;
//     for(int i=0;i<size;i++){
//         ans = ans^i;
//     }
//     cout<<endl;
//     cout<<ans<<endl;
// }

// int main(){
//     int arr[5] = {1,2,3,5,3};
//     repeat(arr,5);
//     return 0;
// }
