#include <iostream>
using namespace std;
 
int main() {
    int arr[5] = {1,2,3,4,5};

    //! name of the array gives the address of the first memory block of the array
    cout << "address of first memory block : " << arr << endl;
    cout << "address of first memory block : " << &arr[0] << endl;

    cout << " value at 0th index : " << *arr<<endl;
    cout << " value at 0th index : " << arr[0]<<endl;
    cout << " value at 0th index + 1 : " << *arr + 1 << endl;
    cout << " value at 1st index : " << *(arr + 1) << endl;

    cout << " value at 2nd index : " << *(arr + 2) << endl;
    cout << " value at 2nd index : " << arr[2] << endl;

    //? this is the other way to print value of array index
    int i = 3;
    cout << " value at 3rd index : " << i[arr] << endl;

    return 0;
}