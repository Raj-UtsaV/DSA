#include <iostream>
#include <vector>
#include <algorithm>
#include <numeric>
using namespace std;

int brute(vector<int> &arr, int n, int days)
{
    int s = *max_element(arr.begin(), arr.end());
    int e = accumulate(arr.begin(), arr.end(), 0);
    for (int i = s; i <= e; i++)
    {
        int d = 1;
        int load = 0;
        for (int j = 0; j < n; j++)
        {
            if (load + arr[j] > i)
            {
                d += 1;
                load = arr[j];
            }
            else
            {
                load += arr[j];
            }
        }
        if (d <= days)
            return i;
    }
    return -1;
}

int optimal(vector<int> &arr, int n, int days) {
    int s = *max_element(arr.begin(), arr.end());
    int e = accumulate(arr.begin(), arr.end(), 0);
    while(s<=e){
        int mid = s + (e - s) / 2;
        int d = 1;
        int load = 0;
        for (int j = 0; j < n; j++)
        {
            if (load + arr[j] > mid)
            {
                d += 1;         
                load = arr[j]; 
            }
            else
            {
                load += arr[j];
            }
        }
        if (d <= days){
            e = mid-1;
        }
        else
            s = mid + 1;
    }
    return s;
}

int main()
{
    vector<int> arr = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
    int n = arr.size();
    int days = 5;
    cout << brute(arr, n, days) << endl;
    cout << optimal(arr, n, days) << endl;
    return 0;
}