#include <iostream>
using namespace std;

int sum(int size)
{
    int arr[10000];
    int ans = 0;

    for (int i = 0; i < size; i++)
    {
        cin >> arr[i];
    }

    for (int i = 0; i < size; i++)
    {
        ans = ans + arr[i];
    }
    cout << endl;
    cout << ans;
    return 0;
}

int main()
{
    int size;
    cin >> size;
    cout << endl;

    sum(size);

    return 0;
}