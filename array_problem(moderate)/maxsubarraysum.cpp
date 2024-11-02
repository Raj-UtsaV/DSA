#include <iostream>
using namespace std;

void brute(int arr[],int n){
    int maxi = INT_MIN;
    for (int i = 0; i < n;i++){
        for (int j = i; j < n;j++){
            int sum = 0;
            for (int k = i; k <= j;k++){
                sum += arr[k];
            }
            maxi = max(sum,maxi);

        }
    }
    cout << maxi << endl;
}
 
void better(int arr[],int n){
    int maxi = INT_MIN;
    for (int i = 0; i < n;i++){
        int sum = 0;
        for (int j = i; j < n;j++){
            sum += arr[j];
            maxi = max(sum, maxi);
        }
    }
    cout << maxi << endl;
}

void best(int arr[],int n){
    int maxi = INT_MIN;
    int index1 = 0;
    int index2 = 0;
    int maxic = 0;
    int sum = 0;
    for (int i = 0; i < n;i++){
        sum += arr[i];
        maxi = max(sum, maxi);
        if(maxic < maxi){
            index2 = i;
            maxic = maxi;
        }

        if(sum<0){
            sum = 0;
            index1 = i;
        }
    }
    cout << maxi << endl;
    for (int i = index1; i <= index2;i++){
        cout << arr[i] << " ";
    }
}

int main() {
    int arr[5] = {1, 2, 3, -4, -1};
    brute(arr, 5);
    better(arr, 5);
    best(arr, 5);
    return 0;
}