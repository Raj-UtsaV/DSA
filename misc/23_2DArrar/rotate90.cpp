#include <iostream>
using namespace std;
 
int main() {
    int matrix[3][3]={{1,2,3},{4,5,6},{7,8,9}};

    int row  = 3;
    int col = 3;

    int eRow = row-1;
    int sRow = 0;
    int sCol = 0;
   

    for(int i=0;i<row;i++){


        for(int j=eRow;j>=sRow;j-- ){
            cout<<matrix[j][sCol]<<" ";
        }
        sCol++;
        
    }


  return 0;
}