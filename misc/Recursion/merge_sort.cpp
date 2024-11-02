#include <iostream>
using namespace std;

void merge(int *arr, int s, int e)
{

    int mid = s + (e - s) / 2;

    int len1 = mid + 1 - s;
    int len2 = e - mid;

    int *first = new int[len1];
    int *second = new int[len2];

    //? copying vaues
    int mainArrayIndex = s;
    for (int i = 0; i < len1; i++)
    {
        first[i] = arr[mainArrayIndex++];
    }

    mainArrayIndex = mid + 1;
    for (int i = 0; i < len2; i++)
    {
        second[i] = arr[mainArrayIndex++];`
    }

    //? mergr 2 sorted arrrays
    int Index1 = 0;
    int Index2 = 0;
    mainArrayIndex = s;

    while (Index1 < len1 && Index2 < len2)
    {
        if (first[Index1] < second[Index2])
        {
            arr[mainArrayIndex++] = first[Index1++];
        }
        else
        {
            arr[mainArrayIndex++] = second[Index2++];
        }
    }

    while (Index1 < len1)
    {
        arr[mainArrayIndex++] = first[Index1++];
    }

    while (Index2 < len2)
    {
        arr[mainArrayIndex++] = second[Index2++];
    }

    delete []first;
    delete []second;
}

void mergeSort(int *arr, int s, int e)
{

    //? base case
    if (s >= e)
        return;

    int mid = s + (e - s) / 2;

    //? left part sort
    mergeSort(arr, s, mid);

    //? right part sort
    mergeSort(arr, mid + 1, e);

    //? merge both
    merge(arr, s, e);
}

int main()
{
    int arr[5] = {1, 2, 4, 3, 9};
    int n = 5;

    mergeSort(arr, 0, n - 1);

    for (auto i: arr)
    {
        cout << i << " ";
    }
    cout << endl;

    return 0;
}