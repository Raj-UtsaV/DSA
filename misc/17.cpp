#include <iostream>
using namespace std;

int main()
{
    int arr[5] = {5, 3, 6, 7, 1};
    int n = 5;
    for (int i = 1; i < n; i++)
    {
        // * for round 1 to n-1

        // ! general code
        // *for (int j = 0; j < n - 1; j++)
        // *{
        // *    if (arr[j] > arr[j + 1])
        // *    {
        // *        swap(arr[j], arr[j + 1]);
        // *    }
        // *}

        // ! enhanced code
        // * in every round end decrease by 1 unit
        bool swapped = false;
        for (int j = 0; j < n - i; j++)
        {

            if (arr[j] > arr[j + 1])
            {
                swap(arr[j], arr[j + 1]);
                swapped = true;
            }
        }
        if (swapped == false)
            break; // * if no number is swapped then
    }
    for (int i = 0; i < n; i++)
    {
        cout << arr[i] << " ";
    }
    return 0;
}