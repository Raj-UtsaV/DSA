#include <iostream>
using namespace std;

int main()
{
    int arr[50000];
    fill_n(arr, 50000, -24);
    for (int i = 0; i < 49999; i++)
    {
        cout << arr[i] << endl;
    }
    return 0;
}