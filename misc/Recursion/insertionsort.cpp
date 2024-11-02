#include <iostream>
using namespace std;

void insertionsort(int arr[], int n)
{
    if (n == 1)
        return;

    insertionsort(arr, n - 1);
    int k = arr[n - 1];
    int j = n - 2;

    while (j >= 0 && arr[j] > k)
    {
        arr[j + 1] = arr[j];
        j--;

    }
    arr[j + 1] = k;
}

int main()
{
    int arr[5] = {5, 4, 2, 3, 1};

    insertionsort(arr, 5);

    for (auto i : arr)
    {
        cout << i << " ";
    }

    return 0;
}