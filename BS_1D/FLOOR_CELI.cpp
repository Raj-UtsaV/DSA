///? lower bound smallest arr[index]>=k

#include <iostream>
using namespace std;

int cli(int arr[], int n, int k)
{
    int s = 0;
    int e = n - 1;
    int ans = n;
    while (s <= e)
    {
        int mid = s + (e - s) / 2;
        if (arr[mid] >= k)
        {
            ans = mid;
            e = mid - 1;
        }
        else
            s = mid + 1;
    }
    if(ans == n)
        return -1;
    return arr[ans];
}

int flr(int arr[], int n, int k)
{
    int s = 0;
    int e = n - 1;
    int ans = n;
    while (s <= e)
    {
        int mid = s + (e - s) / 2;
        if (arr[mid] <= k)
        {
            ans = mid;
            s = mid + 1;
        }
        else
            e = mid - 1;
    }
    if(ans == n)
        return -1;
    return arr[ans];
}

int main()
{
    int a[1] = {2};
    int x = 23;
    // cout << cli(arr, 6, 2) << " ";
    // cout << flr(arr, 6, 2);
    int flr = lower_bound(a, a+1, x) - a;
    int cli = lower_bound(a, a+1, x) - a;

    if(flr == cli && a[flr] != x)
        flr =  - 1;
    if(cli == 1)
        cli = -1;
    cout << flr << cli;
    return 0;
}