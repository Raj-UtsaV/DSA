#include <iostream>
#include <climits>
using namespace std;

int max(int arr[], int size)
{
    int maxi = INT_MIN;
    for (int i = 0; i < size; i++)
    {
        maxi = max(maxi, arr[i]);

        // fd(arr[i]>max){
        //     max=arr[i];
        //  }
    }
    return maxi;
}
int min(int arr[], int size)
{
    int min = INT_MAX;
    for (int i = 0; i < size; i++)
    {
        if (arr[i] < min)
        {
            min = arr[i];
        }
    }
    return min;
}

int main()
{
    int size;
    cin >> size;

    int arr[10000];

    for (int i = 0; i < size; i++)
    {
        cin >> arr[i];
    }
    cout << "max " << max(arr, size) << endl;
    cout << "min " << min(arr, size) << endl;
}