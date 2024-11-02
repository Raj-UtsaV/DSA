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

void sort(int arr[], int size)
{
    int left = 0, right = size - 1;

    while (arr[left] == 0 && left < right)
    {
        left++;
    }

    while (arr[right] == 1 && left < right)
    {
        right--;
    }

    if (/*arr[left]==1 && arr[right]==0 &&*/ left < right)
    {
        swap(arr[left], arr[right]);
        left++;
        right--;
    }
    cout << endl;
}

int main()
{
    int arr[5] = {0, 1, 0, 0, 1};
    sort(arr, 5);
    printArray(arr, 5);

    return 0;
}