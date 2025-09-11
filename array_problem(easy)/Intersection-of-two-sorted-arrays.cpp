#include <iostream>
#include <vector>
using namespace std;

void print(int arr[], int n)
{
    for (int i = 0; i < n; i++)
    {
        cout << arr[i] << " ";
    }
    cout << endl;
}

void intersection_brute(int arr1[], int arr2[], int n1, int n2)
{
    vector<int> v;
    for (int i = 0; i < n1; i++)
    {
        int k = -1;
        for (int j = k + 1; j < n2; j++)
        {
            if (arr1[i] == arr2[j])
            {
                v.push_back(arr1[i]);
                k = j;
                break;
            }
        }
    }

    cout << "Brute : ";
    for (auto i : v)
    {
        cout << i << " ";
    }
    cout << endl;
}

void intersection_optimal(int arr1[], int arr2[], int n1, int n2)
{
    int i = 0;
    int j = 0;
    vector<int> v;

    while (i < n1 && j < n2)
    {
        if (arr1[i] < arr2[j])
        {
            i++;
        }
        else if (arr1[i] > arr2[j])
        {
            j++;
        }

        else
        {
            v.push_back(arr1[i]);
            i++;
            j++;
        }
    }

    cout << "Optimal : ";
    for (auto i : v)
    {
        cout << i << " ";
    }
    cout << endl;
}

int main()
{
    int arr1[5] = {1, 1, 2, 3, 4};
    int arr2[4] = {1, 1, 4, 6};

    int n1 = sizeof(arr1) / sizeof(arr1[0]);
    int n2 = sizeof(arr2) / sizeof(arr2[0]);

    cout << "Given Arrays " << endl;
    print(arr1, n1);
    print(arr2, n2);

    intersection_brute(arr1, arr2, n1, n1);
    intersection_optimal(arr1, arr2, n1, n1);

    return 0;
}