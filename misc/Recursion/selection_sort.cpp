#include <iostream>
using namespace std;

int minelemindex(int arr[],int n,int index){

    if(index == n)
        return index;

    int k = minelemindex(arr, n, index+1);

    return (arr[index] < arr[k]) ? index : k;
}

void selectionsort(int *arr,int n,int index = 0){
    if( index == n )
        return;

    int k = minelemindex(arr, n-1 ,index);

    swap(arr[index], k[arr]);

    selectionsort(arr , n ,index + 1);
}
 
int main() {
    int arr[5] = {1, 4, 2, 4, 3};
    selectionsort(arr, 5);

    for (int i = 0; i < 5;i++)
    {
        cout << arr[i] << " ";
    }

    return 0;
}