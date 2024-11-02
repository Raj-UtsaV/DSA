#include <iostream>
#include <algorithm>
using namespace std;

void print(int arr[], int n)
{
    for (int i = 0; i < n; i++)
    {
        cout << arr[i] << " ";
    }
    cout << endl;
}

void set_array_to_default(int arr[], int n)
{
    for (int i = 0; i < n; i++)
    {
        arr[i] = i + 1;
    }
}

void by1index(int arr[], int n)
{
    int temp = arr[0];
    for (int i = 1; i < n; i++)
    {
        arr[i - 1] = arr[i];
    }
    arr[n - 1] = temp;

    cout << "BY 1 Index : ";
    print(arr, n);
    set_array_to_default(arr, n);
}

void by_k_index_brute(int arr[], int n, int k)
{

    // todo brute
    while (k--)
    {
        int temp = arr[0];
        for (int i = 1; i < n; i++)
        {
            arr[i - 1] = arr[i];
        }
        arr[n - 1] = temp;
    }
    cout << "BY K Index (brute) : ";
    print(arr, n);
    set_array_to_default(arr, n);
}

void by_k_index_better(int arr[], int n, int k)
{

    int arr1[k] = {0};
    for (int i = 0; i < k; i++)
    {
        arr1[i] = arr[i];
    }

    // todo shifting
    for (int i = k; i < n; i++)
    {
        arr[i - k] = arr[i];
    }

    for (int i = n - k; i < n; i++)
    {
        arr[i] = arr1[i - (n - k)];
    }

    cout << "BY K Index (better) : ";
    print(arr, n);
    set_array_to_default(arr, n);
}

void by_k_index_best(int arr[], int n, int k)
{
    reverse(arr, arr + k);
    print(arr, n);
    reverse(arr + k, arr + n);
    print(arr, n);
    reverse(arr, arr + n);
    print(arr, n);
    cout << "BY K Index (best) : ";
    print(arr, n);
    set_array_to_default(arr, n);
}

int main()
{
    int arr[7] = {1, 2, 3, 4, 5, 6, 7};
    int n = 7;

    cout << "Given Array : ";
    print(arr, n);

    by1index(arr, n);
    int k = 3;
    int k1 = k % n;
    by_k_index_brute(arr, n, k1);
    by_k_index_better(arr, n, k1);
    by_k_index_best(arr, n, k1);

    return 0;
}