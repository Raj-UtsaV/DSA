#include <iostream>
#include <algorithm>
using namespace std;

bool ispossible(int mid, int k, int m, int arr[], int n)
{
  int count = 0;
  int ans = 0;
  for (int i = 0; i < n; i++)
  {
    if (arr[i] <= mid)
    {
      count++;
    }
    else
    {
      ans += count / k;
      count = 0;
    }
  }
  ans += count / k;
  return ans >= m;
  ans = 0;
}

int brute(int arr[], int n, int k, int m)
{
  int count = 0;
  int ans = 0;
  int s = *min_element(arr, arr + n);
  int e = *max_element(arr, arr + n);
  for (int j = s; j <= e; j++)
  {

    for (int i = 0; i < n; i++)
    {

      if (arr[i] <= j)
      {
        count++;
      }

      else
      {
        ans += count / k;
        count = 0;
      }
    }
    ans += count / k;
    count = 0;
    if (ans >= m)
      return j;
    else
      ans = 0;
  }
  return ans;
}

int optimal(int arr[], int n, int k, int m)
{
  int s = *min_element(arr, arr + n);
  int e = *max_element(arr, arr + n);
  while (s <= e)
  {
    int mid = s + (e - s) / 2;
    int x = ispossible(mid, k, m, arr, n);
    if (x == 0)
      s = mid + 1;
    else
      e = mid - 1;
  }
  return s;
}

int main()
{
  int arr[] = {1, 10, 3, 10, 2};
  int n = sizeof(arr) / sizeof(arr[0]);
  int m = 3;
  int k = 1;

  long long j = (1LL * m * k) % 1000000007;
  if (j > n)
    cout
        << "-1";
  else
  {
    cout << brute(arr, n, k, m) << endl;
    cout << optimal(arr, n, k, m) << endl;
  }

  return 0;
}