#include <iostream>
using namespace std;

void print(int arr[], int n)
{
    for (int i = 0; i < n; i++)
    {
        cout << arr[i] << " ";
    }
    cout << endl;
}

void find_brute(int arr[], int n)
{
    int flag = 1;
    for (int i = 1; i <= n + 1; i++)
    {
        for (int j = 0; j < n; j++)
        {
            if (arr[j] == i)
            {
                flag = 0;
            }
        }

        if (flag)
        {

            cout << "Brute : " << i<<endl;
            return;
        }
        flag = 1;
    }
}

void find_better(int arr[], int n)
{
    int arr1[n + 1] = {0};
    for (int i = 0; i < n; i++)
    {
        arr1[arr[i]]++;
    }
    for (int i = 1; i < n + 1; i++)
    {
        if (arr1[i] == 0)
        {
            cout << "Better : " << i << endl;
            
            return;
        }
    }
}

void find_optimal(int arr[],int n){
    int k = ((n + 1) * (n + 2)) / 2;
    int sum = 0;
    for (int i = 0; i < n;i++){
        sum += arr[i];
    }
    cout << "OPtimal : " << k - sum << endl;
}

void find_optimal_XOR(int arr[],int n){

}

int main()
{
    int arr[7] = {1, 2, 4, 6, 8, 5, 3};

    cout << "Given Arrays " << endl;
    print(arr, 7);

    find_brute(arr, 7);
    find_better(arr, 7);
    find_optimal(arr, 7);
    find_optimal_XOR(arr, 7);

    return 0;
}