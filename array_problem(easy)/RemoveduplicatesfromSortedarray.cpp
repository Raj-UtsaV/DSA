#include <iostream>
#include<set>
using namespace std;
 
int main() {
    int arr[5] = {1, 3, 4, 4, 5};

    //todo better
    // set<int> s;
    // for (int i = 0; i < 5;i++){
    //     s.insert(arr[i]);
    // }
    // for(auto i:s){
    //     cout << i << " ";
    // }
    // cout << endl;
    // cout << s.size();

    //todo best
    int j = 0;
    for (int i = 1; i < 5;i++){
        if(arr[i] != arr[j]){
            j++;
            arr[j] = arr[i];
        }
    }
    for (int i = 0; i <= j;i++){
        cout << arr[i] << " ";
    }
        return 0;
}