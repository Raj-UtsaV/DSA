#include <iostream>
#include <set>
#include<vector>
using namespace std;

void print(int arr[], int n)
{
    for (int i = 0; i < n; i++)
    {
        cout << arr[i] << " ";
    }
    cout << endl;
}

void brute(int arr1[], int arr2[], int n1, int n2)
{
    set<int> s;

    for (int i = 0; i < n1; i++)
    {
        s.insert(arr1[i]);
    }

    for (int i = 0; i < n2; i++)
    {
        s.insert(arr2[i]);
    }

    cout << "Brute " << endl;
    cout << "no. of different elements : " << s.size() << endl;
    for (auto i : s)
    {
        cout << i << " ";
    }
    cout << endl;
}

void best(int arr1[], int arr2[], int n1, int n2)
{
    int i = 0, j = 0;
    vector<int> unionArr;

    while (i < n1 && j < n2)
    {
        if (arr1[i] <= arr2[j])
        {
            if (unionArr.size() == 0 || unionArr.back() < arr1[i])
            {
                unionArr.push_back(arr1[i]);
            }
            i++;
        }

        else
        {
            if (unionArr.size() == 0 || unionArr.back() < arr2[j])
            {
                unionArr.push_back(arr2[j]);
            }
            j++;
        }

        while (i < n1)
        {
            if (unionArr.size() == 0 || unionArr.back() < arr1[i])
            {
                unionArr.push_back(arr1[i]);
            }
            i++;
        }

        while (j < n2)
        {
            if (unionArr.size() == 0 || unionArr.back() < arr2[j])
            {
                unionArr.push_back(arr2[j]);
            }
            j++;
        }

        cout << "Best " << endl;
        cout << "no. of different elements : " << unionArr.size() << endl;
        for (auto i : unionArr)
        {
            cout << i << " ";
        }
        cout << endl;
    }
}

int main()
{
    int arr1[5] = {1, 1, 2, 3, 4};
    int arr2[4] = {1, 6, 4, 1};

    int n1 = sizeof(arr1) / sizeof(arr1[0]);
    int n2 = sizeof(arr2) / sizeof(arr2[0]);

    cout << "Given Arrays " << endl;
    print(arr1, n1);
    print(arr2, n2);

    brute(arr1, arr2, n1, n2);
    best(arr1, arr2, n1, n2);

    return 0;
}