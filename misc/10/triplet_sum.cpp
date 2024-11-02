#include <iostream>
#include <vector>
using namespace std;

void tripletSum(int arr[], int size, int target)
{
    vector<int> value1;
    vector<int> value2;
    vector<int> value3;

    for (int i = 0; i < size; i++)
    {
        for (int j = i + 1; j < size; j++)
        {
            for (int k = i + 2; k < size; k++)
            {
                if ((arr[i] + arr[j] + arr[k]) == target)
                {
                    value1.push_back(arr[i]);
                    value2.push_back(arr[j]);
                    value3.push_back(arr[k]);
                }
            }
        }
        for (int i : value1)
            cout << "i = " << i << endl;

        // for (int i = 0, j = 2, k = 2; i < value1.size(), j < value2.size(), k < value3.size(); i++, j++, k++)
        // {
        //     cout << value1[i] << " " << value2[j] << " " << value3[k] << " "<<endl;
        // }
    }
}

int main()
{
    int size;
    cin >> size;

    int arr[10000];
    for (int i = 0; i < size; i++)
    {
        cin >> arr[i];
    }

    int target = target;
    cin >> target;

    tripletSum(arr, size, target);
    return 0;
}