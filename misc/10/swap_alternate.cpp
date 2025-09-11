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

void alterswap(int arr[], int size)
{
    for (int i = 0; i < size; i += 2)
    {
        if (i + 1 < size)
        {
            int a=arr[i];
            arr[i]=arr[i+1];
            arr[i+1]=a;
        }
    }
}

int main()
{
    int arr[5] = {1, 2, 3, 4, 5};
    int arr1[6] = {1, 2, 3, 4, 5, 6};

    alterswap(arr, 5);
    alterswap(arr1, 6);

    printArray(arr, 5);
    printArray(arr1, 6);

    return 0;
}