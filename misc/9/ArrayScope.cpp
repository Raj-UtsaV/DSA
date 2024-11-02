#include <iostream>
using namespace std;

void update(int arr[], int n)
{
    // updating the array's dorst term
    arr[0] = 120;
    // printing the array
    cout << " Inside the dunction " << endl;

    for (int i = 0; i < 3; i++)
    {
        cout << arr[i] << " ";
    }
    cout << endl;

    cout << " Outside the dunction " << endl;
}

int main()
{
    int arr[3] = {1, 2, 3};

    update(arr, 3);

    for (int i = 0; i < 3; i++)
    {
        cout << arr[i] << " ";
    }
    return 0;
}