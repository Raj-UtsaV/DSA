#include <iostream>
using namespace std;

int main()
{
    int arr[2][2] = {{1, 2}, {3, 4}};

    //! print
    for (int col = 0; col < 2; col++)
    {
        if (col & 1)
        {
            for (int row = 1; row >= 0; row--)
            {
                cout << arr[row][col] << " ";
            }
        }
        else
        {
            for (int row = 0; row < 2; row++)
            {
                cout << arr[row][col] << " ";
            }
        }
    }

    cout << endl;

    return 0;
}