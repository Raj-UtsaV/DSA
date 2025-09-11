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

void once_brute(int arr[],int n){
    for (int i = 0; i < n;i++){
        int cnt = 0;
        for (int j = 0; j < n;j++){
            if(arr[j] == arr[i])
                cnt++;
        }
        if(cnt == 1){
            cout << "Brute : " << arr[i] << endl;
        }
    }
}

void once_better(int arr[],int n){
    
}

int main() {
    int arr[7] = {1,1,2,3,3,4,4};

    cout << "Given Arrays " << endl;
    print(arr, 7);

    once_brute(arr, 7);
    once_better(arr, 7);

    return 0;
}