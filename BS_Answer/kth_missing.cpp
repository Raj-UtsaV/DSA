#include <iostream>
using namespace std;

int kth_missing(int *arr, int n, int k)
{
    int s = 0;
    int e = n - 1;
    while (s <= e)
    {
        int mid = s + (e - s) / 2;
        int missing = arr[mid] - (mid + 1);
        if (missing < k)
        {
            s = mid + 1;
        }
        else
        {
            e = mid - 1;
        }
    }
    return k + e + 1;
}

int main()
{
    int arr[] = {2};
    int n = sizeof(arr) / sizeof(arr[0]);
    int k = 1;
    cout << kth_missing(arr, n, k);
    return 0;
}