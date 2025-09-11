#include <iostream>
#include <map>
using namespace std;

void better(int arr[], int n)
{
    map<int, int> m;
    for (int i = 0; i < n;i++){
        m[arr[i]]++;
    }
    for(auto i:m){
        if(i.second>(n/2)){
            cout << i.first << " ";
        }
    }

}

void best(int arr[],int n){
    int cnt = 0;
    int ele;
    for (int i = 0; i < n;i++){
        if(cnt == 0){
            cnt++;
            ele = arr[i];
        }
        else if(cnt != 0 && ele == arr[i]){
            cnt++;
        }
        else
            cnt--;
    }
    cout << ele;
    
}

int main()
{
    int arr[5] = {2, 2, 2, 4, 1};
    better(arr, 5);
    cout << endl;
    best(arr, 5);
    return 0;
}