#include <iostream>
using namespace std;

bool issorted(int arr[], int size)
{
    if (size == 0 || size == 1)
        return true;

    if (arr[0] > arr[1])
        return false;

    return issorted(arr + 1, size - 1);
}

int sum(int arr[], int size)
{

    if (size <= 0)
        return 0;

    return sum(arr, size - 1) + arr[size - 1];
}

string search(int arr[], int size, int key)
{
    if (*arr == key)
        return "Found";
    if (size <= 0)
        return "Not found";

    return search(arr + 1, size - 1, key);
}

string Binarysearch(int arr[], int size, int key)
{

    int mid = size / 2;
    if (arr[mid] == key)
        return "Found";

    if (size <= 0 || size == 1)
        return "Not found";

    if (key > arr[mid])
        return Binarysearch(arr + mid, size - mid, key);
    if (key < arr[mid])
        return Binarysearch(arr, size - mid, key);
}

string Binarysearch1(int arr[], int s, int e, int key)
{

    if (s > e)
        return "Not found";

    int mid = s + (e - s) / 2;


    if (arr[mid] == key)
        return "Found";

    if (key > arr[mid])
        return Binarysearch1(arr, mid + 1, e, key);

    return Binarysearch1(arr, s, mid - 1, key);
}

int main()
{
    int arr[5] = {1, 2, 3, 5, 7};

    if (issorted(arr, 5))
        cout << "Sorted" << endl;

    else
        cout << "Not Sorted" << endl;

    cout << "sum is : " << sum(arr, 5) << endl;
    cout << search(arr, 5, 8) << endl;
    cout << Binarysearch(arr, 5, 5) << endl;
    cout << Binarysearch1(arr, 0, 4, 5) << endl;

    return 0;
}