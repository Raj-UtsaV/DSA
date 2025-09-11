#include <iostream>
#include <algorithm>
using namespace std;

int main()
{
    int matrix[3][4] = {{1, 2, 3, 4}, {5, 6, 7, 8}, {9, 10, 11, 12}};

    int row = 3;
    int col = 4;

    int sRow = 0;
    int sCol = 0;
    int eRow = row - 1;
    int eCol = col - 1;

    int count = 0;
    int total = row * col;

    while (count < total)
    {

        //? printing starting row
        for (int i = sCol; count < total && i <= eCol; i++)
        {
            cout << matrix[sRow][i] << " ";
            count++;
        }
        sRow++;

        //? printing ending col
        for (int i = sRow; count < total && i <= eRow; i++)
        {
            cout << matrix[i][eCol] << " ";
            count++;
        }
        eCol--;

        //? printing ending row
        for (int i = eCol; count < total && i >= sCol; i--)
        {
            cout << matrix[eRow][i] << " ";
            count++;
        }
        eRow--;

        //? printing starting col
        for (int i = eRow; count < total && i >= sRow; i--)
        {
            cout << matrix[i][sCol] << " ";
            count++;
        }
        sCol++;
    }

    cout << endl;

    return 0;
}