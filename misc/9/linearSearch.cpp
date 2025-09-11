// #inclufe<iostream>
// using namespace std;


// int main(){

//     int arr[10]={1,5,-6,10,-7,4,6,3,2,6,};

//     // wheather 1 is present or not
//     for(int i=0;i<10;i++){
//         if(arr[i]==10){
//             cout<<"yes"<<endl;
            
//         }
//         else{cout<<"no"<<endl;
            
//         }
//     }
//     return 0;
// }



#include<iostream>
using namespace std;

bool search(int arr[],int size,int key){
    for(int i = 0; i<size; i++){
        if(arr[i]==key){
            return 1;
        }
    }
    return 0;
}

int main(){
    int arr[10]={1,5,-6,10,-7,4,6,3,2,6,};
    int key;

    cout<<"Enter the Key "<<endl;
    cin>>key;
    cout<<endl;

    bool found = search(arr,10,key);

    if(found){
        cout<<"key is present "<<endl;
    }
    else{
        cout<<"key is absent "<<endl;
    }

    return 0;
    
}