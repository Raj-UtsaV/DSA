#include <iostream>
using namespace std;

int partition(int arr[], int s, int e)
{
    int pivot = arr[s];
    int count = 0;

    for (int i = s + 1; i <= e; i++)
    {
        if (pivot >= arr[i])
        {
            count++;
        }
    }

    int pivotindex = s + count;

    swap(arr[s], arr[pivotindex]);

    int i = s;
    int j = e;
    while (i < pivotindex && j > pivotindex)
    {

        while (arr[i] < pivot)
        {
            i++;
        }

        while (arr[j] > pivot)
        {
            j--;
        }

        if (i < pivotindex && j > pivotindex)
        {
            swap(arr[i++], arr[j--]);
           
        }
    }

    return pivotindex;
}

void quicksort(int arr[], int s, int e)
{
    //? base case
    if (s >= e)
        return;

    //?partition
    int p = partition(arr, s, e);

    // todo recursive call
    quicksort(arr, s, p - 1);
    quicksort(arr, p + 1, e);
}

int main()
{
    int arr[5] = {3, 4, 1, 5, 2};
    quicksort(arr, 0, 4);

    for (auto i : arr)
    {
        cout << i << " ";
    }
    return 0;
}