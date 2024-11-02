// /..try

// #include<iostream>
// using namespace std;

// int main(){
//     int arr[6]={1,2,3,4,5,6};
//     for(int i =1 ; i<6 ;i++){
//         arr[i-1]=arr[6-i];

//     }

//     for(int i=0;i<6;i++){
//         cout<<arr[i]<<" ";
//     }
//     return 0;
}

#include <iostream>
using namespace std;

void printArray(int arr[], int size)
{
    for (int i = 0; i < size; i++)
    {
        cout << arr[i] << " ";
    }
    cout << endl;
}

void reverse(int arr[], int size)
{
    int start = 0;
    int end = size - 1;

    while (start <= end)
    {
        swap(arr[start], arr[end]);
        start++;
        end--;
    }
}

int main()
{
    int arr[6] = {1, 2, 3, 4, 5, 6};
    int arr1[5] = {1, 2, 3, 4, 5};

    reverse(arr, 6);
    reverse(arr1, 5);

    printArray(arr, 6);
    printArray(arr1, 5);

    return 0;
}