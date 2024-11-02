#include <iostream>
using namespace std;
 
int main() {

    int column;
    cout << "Enter the no of columns : ";
    cin >> column;

    int row;
    cout << "Enter the no of Rows : ";
    cin >> row;

    int **arr = new int *[column]; //? No. of columns (array)

    for (int i = 0; i < column;i++){
        arr[i] = new int[row]; //? No. of rows (array)
    }
    cout << endl;

    //* Creation Done

    //* Taking input
    cout << "Input Data " << endl;
    for (int i = 0; i < column; i++){
        for (int j = 0; j < row;j++){
            cin >> arr[i][j];
        }
    }

    cout << endl<<"Output"<<endl;

    //* Taking Output
    
    for (int i = 0; i < column; i++)
    {
        for (int j = 0; j < row; j++)
        {
            cout << arr[i][j] <<" ";
        }
        cout << endl;
    }


    //* Releasing Memory
    for (int i = 0; i < column; i++)
    {
        delete [] arr[i]; //? No. of rows (array)
    }

    delete[] arr;

    return 0;
}