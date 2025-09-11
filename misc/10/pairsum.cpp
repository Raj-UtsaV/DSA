#include <iostream>
#include <vector>
using namespace std;

void pairsum(int arr[], int size)
{
    vector<int> value;
    vector<int> value1;

    for (int i = 0; i < size; i++)
    {
        for (int j = i + 1; j < size; j++)
        {
            if ((arr[i] + arr[j]) == 5)
            {
                value.push_back(i);
                value1.push_back(j);
            }
        }
    }

    for (int i = 0, j = 0; i < value.size(), j < value1.size(); i++, j++)
    {
        cout << value[i] << value1[j] << endl;
    }
}

int main()
{
    int arr[5] = {1, 2, 3, 4, 5};
    pairsum(arr, 5);
    return 0;
}