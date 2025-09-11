#include <iostream>
#include <vector>
#include <numeric>
#include <algorithm>
using namespace std;

int ispossible(vector<int> &arr, int n, int cmp)
{
    int student = 1;
    int page = 0;
    for (int i = 0; i < n; i++)
    {
        if (page + arr[i] <= cmp)
        {
            page += arr[i];
        }
        else
        {
            student++;
            page = arr[i];
        }
    }
    return student;
}

int brute(vector<int> &arr, int n, int m)
{
    int e = accumulate(arr.begin(), arr.end(), 0);
    int s = *max_element(arr.begin(), arr.end());
    if (m > n)
    {
        return -1;
    }
    for (int i = s; i < e; i++)
    {
        if (ispossible(arr, n, i) == m)
            return i;
    }
    //?dummy return
    return s;
}

int optimal(vector<int> &arr, int n, int m)
{
    int e = accumulate(arr.begin(), arr.end(), 0);
    int s = *max_element(arr.begin(), arr.end());
    if (m > n)
        return -1;

    while (s <= e)
    {
        int mid = s + (e - s) / 2;
        int ans = ispossible(arr, n, m);
        if (ans > m)
        {
            //? if student needed is more than required isliye hme ek student to jyada page dene ki need hai
            s = mid + 1;
        }
        else
            e = mid - 1;
    }
    return s;
}

int main()
{
    vector<int> arr = {1, 17, 14, 9, 15, 9, 14};
    int n = arr.size();
    int k = 7;
    cout << brute(arr, n, k) << endl;
    cout << optimal(arr, n, k) << endl;

    return 0;
}