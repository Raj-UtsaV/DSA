#include <iostream>
using namespace std;


int largestRowSum(int arr[][4],int row,int col){
    int maxi = INT_MIN;
    int rowIndex = -1;

    for(int row = 0;row<3;row++){
        int sum = 0;

        for(int col = 0;col<4;col++){
            sum+=arr[row][col];
        }
        if(sum > maxi){
            maxi = sum;
            rowIndex = row;
        }


    }

    cout<<"Largest sum is : "<<maxi<<endl<<"Row is : " ;
    return rowIndex;
}
 
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


    //!print
    for(int row = 0;row<3;row++){
        for(int col=0;col<4;col++){
            cout<<arr[row][col]<<" ";
        }
        cout<<endl;
    }

    cout<<endl;


    cout<<largestRowSum(arr,3,4);
     




    


  return 0;
}