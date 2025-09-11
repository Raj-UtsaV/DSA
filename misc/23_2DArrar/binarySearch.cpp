#include <iostream>
#include <string>
using namespace std;

bool Search(int matrix[][4], int target, int row, int col)
{

    int start = 0;
    int end = row * col - 1;
    int mid = start + (end - start) / 2;

    while (start <= end)
    {
        int element = matrix[mid / col][mid % col];

        if (element == target)
            return true;
        else if (element < target)
            start = mid + 1;
        else
            end = mid - 1;

        mid = start + (end - start) / 2;
    }
    return false;
}

int main()
{
    int matrix[3][4] = {{1, 3, 5, 7}, {10, 11, 16, 20}, {23, 30, 34, 60}};
    int target = 3;

    cout << Search(matrix, target, 3, 4);

    return 0;
}