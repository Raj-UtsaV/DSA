#include <iostream>
using namespace std;

void set_array_to_default(int arr[], int n)
{
    int arr1[n] = {1, 0, 2, 3, 0, 1, 0, 4};
    for (int i = 0; i < n; i++)
    {
        arr[i] = arr1[i];
    }
}

void print(int arr[], int n)
{
    for (int i = 0; i < n; i++)
    {
        cout << arr[i] << " ";
    }
    cout << endl;
    set_array_to_default(arr, n);
}

void move_to_end_brute(int arr[], int n)
{
    int arr1[n] = {0};
    int j = 0;
    for (int i = 0; i < n; i++)
    {
        if (arr[i] != 0)
        {
            arr1[j] = arr[i];
            j++;
        }
    }
    cout << "Brute : ";
    print(arr1, n);
}

void move_to_end_best(int arr[], int n)
{

    int j = -1;
    for (int i = 0; i < n; i++)
    {
        if (arr[i] == 0)
        {
            j = i;
            break;
        }
    }

    if (j == -1)
    {
        cout << "BEST : ";
        print(arr, n);
        return;
    }

    for (int i = j + 1; i < n; i++)
    {
        if (arr[i] > 0)
        {
            swap(arr[j], arr[i]);
            j++;
        }
    }
    cout << "BEST : ";
    print(arr, n);
}

int main()
{
    int arr[8] = {1, 0, 2, 3, 0, 1, 0, 4};
    int n = sizeof(arr) / sizeof(arr[0]);
    cout << "Given Array : ";
    print(arr, n);

    move_to_end_brute(arr, n);
    move_to_end_best(arr, n);

    return 0;
}