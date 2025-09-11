#include <iostream>
using namespace std;

int main()
{
    int arr[5] = {7, 1, 4, 3, 9};
    int n = 5;

    for (int i = 0; i < n; i++)
    {
        for (int j = i + 1; j < n; j++)
        {
            if (arr[i] > arr[j])
            {
                int p = arr[i];
                arr[i] = arr[j];
                arr[j] = p;
            }
        }
    }
    for (int i = 0; i < 5; i++)
    {
        cout << arr[i] << " ";
    }
    return 0;
}