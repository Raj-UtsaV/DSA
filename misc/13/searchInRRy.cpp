#include <iostream>
using namespace std;

int search(int arr[], int s, int e, int key)
{
    int start = s;
    int end = e;

    int mid = start + (end - start) / 2;

    while (start <= end)
    {

        if (arr[mid] == key)
        {
            return mid;
        }

        if (key > arr[mid])
        {
            start = mid + 1;
        }

        if (key < arr[mid])
        {
            end = mid - 1;
        }

        mid = start + (end - start) / 2;
    }
    return -1;
}

int pivot(int arr[], int size)
{

    int s = 0;
    int e = size - 1;
    int mid = s + (e - s) / 2;

    while (s < e)
    {
        if (arr[mid] >= arr[0])
        {
            s = mid + 1;
        }
        else
        {
            e = mid;
        }
        mid = s + (e - s) / 2;
    }
    return s;
}

int main()
{
    int arr[9] = {10 ,11, 1, 2, 3, 4, 5, 6, 9};
    int n = 9;
    int key;
    cin >> key;
    int pivo = pivot(arr, n - 1);
    if (key >= arr[pivo] && key <= arr[n - 1])
    {
        cout << search(arr, pivo, n - 1, key);
    }
    else
    {
        cout << search(arr, 0, pivo, key);
    }
    return 0;
}