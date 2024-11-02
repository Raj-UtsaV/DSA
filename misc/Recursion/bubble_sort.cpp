#include <iostream>
using namespace std;

void bubblesort(int *arr, int n)
{
    // TODO : Base case
    if (n == 0 || n == 1)
        return;

    // TODO : 1st largest element get sorted
    for (int i = 0; i < n - 1; i++) //? here n-1 is taken bcs if i=n-1 then i+1 = n which doesn't exist
    {
        if (arr[i] > arr[i + 1])
        {
            swap(arr[i], arr[i + 1]);
        }
    }

    bubblesort(arr, n - 1);
}

int main()
{
    int arr[5] = {1, 3, 4, 4, 6};
    bubblesort(arr, 5);

    for (int i = 0; i < 5; i++)
    {
        cout << arr[i] << " ";
    }

    return 0;
}
