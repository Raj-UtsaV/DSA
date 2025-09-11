#include <iostream>
using namespace std;

void print(int arr[],int n,int start = 0){
    for (int i = start; i < n;i++){
        cout << i[arr] << " ";
    }
}
 
int main() {
    int arr[5] = {1, 2, 3, 4, 6};

    cout << "without start value" << endl;
    print(arr, 5);
    cout << endl;

    cout << "with start value" << endl;
    print(arr, 5, 2);

    return 0;
}