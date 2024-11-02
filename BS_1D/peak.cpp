#include <iostream>
#include <vector>
using namespace std;

int peak_brute(vector<int> &v, int n)
{

    for (int i = 0; i < n; i++)
    {
        if (i == 0 && v[i + 1] < v[i])
            return v[i];
        if (i == n - 1 && v[n - 2] < v[n - 1])
            return v[n - 1];
        if (v[i] > v[i + 1] && v[i] > v[i - 1])
            return v[i];
    }
    return -1;
}

int peak_better(vector<int> &v, int n)
{
    int low = 0;
    int high = n - 1;

    while (low < high)
    {
        int mid = low + (high - low) / 2;

        if (v[mid] > v[mid - 1] && v[mid] > v[mid + 1])
            return v[mid];
        // If the middle element is smaller than the next one, the peak must be on the right side
        if (v[mid] > v[mid - 1])
        {
            low = mid + 1;
        }
        // If the middle element is greater than the next one, the peak must be on the left side
        else if (v[mid] > v[mid + 1])
        {
            high = mid;
        }
    }

    return -1;
}

/// @brief this code can be fail for some inputs
int peak_better2(vector<int> v, int n)
{
    int low = 0;
    int high = n - 1;
    int mid = low + (high - low) / 2;
    while (low <= high)
    {
        mid = low + (high - low) / 2;
        if (v[mid] > v[mid - 1] && v[mid] > v[mid + 1])
            return v[mid];
        else if (v[low] <= v[mid])
        {
            low = mid + 1;
        }
        else if (v[mid] >= v[high])
            high = mid - 1;
    }
    return v[mid];
}

int main()
{
    vector<int> v = {1, 2, 3, 2, 1, 6, 7, 8};
    int n = v.size();
    cout << peak_brute(v, n) << endl;
    cout << peak_better(v, n) << endl;
    cout << peak_better2(v, n) << endl;

    return 0;
}