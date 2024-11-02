#include <iostream>
using namespace std;

int pivot(int *arr, int n)
{
    int s = 0;
    int e = n - 1;
    int ans = INT_MAX;
    int ansindex = 0;
    while (s <= e)
    {
        int mid = s + (e - s) / 2;

        if (arr[s] <= arr[e])
        {
            ans = min(arr[s], arr[e]);
            break;
        }

        else if (arr[s] <= arr[mid])
        {
            if (arr[s] < ans)
            {
                ans = arr[s];
                ansindex = s;
            }
            s = mid + 1;
        }
        else if (arr[mid] <= arr[e])
        {
            if (arr[e] < ans)
            {
                ans = arr[mid];
                ansindex = mid;
            }
            e = mid - 1;
        }
    }
    return ansindex;
}

int main()
{
    int arr[5] = {4, 5, 1, 2, 3};
    cout << pivot(arr, 5);

    return 0;
}