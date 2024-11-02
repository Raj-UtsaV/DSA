#include <iostream>
using namespace std;


int main() {
    int arr[3][4];
    
    

    //!input row wise
    for(int row = 0;row<3;row++){
        for(int col=0;col<4;col++){
            cin>>arr[row][col];
        }
    }


    // //!input col wise
    // for(int col = 0;col<4;col++){
    //     for(int row=0;row<3;row++){
    //         cin>>arr[row][col];
    //     }
    // }


    //!print with row sum
    for(int row = 0;row<3;row++){
        int sum = 0;
        for(int col=0;col<4;col++){
            sum += arr[row][col];
            cout<<arr[row][col]<<" ";
        }
        cout<<"   "<<sum;
        cout<<endl;
    }

    cout<<endl;

    //!print with col sum
    for(int col = 0;col<4;col++){
        int sum = 0;
        for(int row=0;row<3;row++){
            sum += arr[row][col];
            cout<<arr[row][col]<<" ";
        }
        cout<<"   "<<sum;
        cout<<endl;
    }

    cout<<endl;


  return 0;
}