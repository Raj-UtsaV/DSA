#include <iostream>
using namespace std;

int getsum(int *arr,int n){

    int sum = 0;

    for (int i = 0; i < n;i++){
        sum += arr[i];
    }

    return sum;
}
 
int main() {

    int n;
    cout << "Enter the size of array : ";
    cin >> n;

    //TODO : Variable size array
    int *arr = new int[n];

    //TODO: Taking input in array
    for (int i = 0; i < n;i++){
        cin >> arr[i]; //? = *(arr + i)
    }

    int ans = getsum(arr, n);

    cout << "The sum of all the elements of array is : " << ans << endl;


    //* khatarnak chiz system crash
    // while(true){
    //     int *p = new int;
    // }

    return 0;
}