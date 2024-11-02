#include <iostream>
using namespace std;

int single_brute(int *arr, int n)
{
    for (int i = 0; i < n; i++)
    {

        if (arr[i] != arr[i + 1] && arr[i] != arr[i - 1])
        {
            return arr[i];
        }
    }
    return -1;
}

int single_best(int *arr, int n)
{

    if (n == 1)
        return arr[0];

    if (arr[0] != arr[1])
        return arr[0];

    if (arr[n - 1] != arr[n - 2])
        return arr[n - 1];

    int s = 1;
    int e = n - 2;

    while (s <= e)
    {

        int m = s + (e - s) / 2;
        // todo :? Check if the middle element is single
        if (arr[m] != arr[m - 1] && arr[m] != arr[m + 1])
            return arr[m];

        // todo : If the middle index is even, the single element must be in the left half
        // todo : if the middle element is equal to its left neighbor, or in the right half
        // todo : if the middle element is equal to its right neighbor
        else if ((m % 2 == 1 && arr[m] == arr[m - 1]) || (m % 2 == 0 && arr[m] == arr[m + 1]))
        {
            // todo : Move the search space to the right half
            s = m + 1;
        }

        // todo : Otherwise, the single element must be in the right half
        else
        {
            // todo : Move the search space to the left half
            e = m - 1;
        }
        // todo :? If no single element is found, return -1
    }
    return -1;
}

int main()
{
    int arr[7] = {1, 1, 2, 2, 3, 4, 4};
    int n = sizeof(arr) / sizeof(arr[0]);
    cout << single_brute(arr, n) << endl;
    cout << single_best(arr, n) << endl;
    return 0;
}