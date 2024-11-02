#include <iostream>
using namespace std;
 
int main() {

    //int arr[10] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};

//! 1 -> size
    // cout <<" size of array in memeory : "<<  sizeof(arr)<<endl;
    // cout <<" size of array 0th index : "<<  sizeof(*arr)<<endl;
    // cout << " address of 0th index : " << &arr << endl;

    // int *ptr = &arr[0];
    // cout <<" size of pointer : " <<  sizeof(ptr) << endl;
    // cout <<" size of value stored at pointer  : " <<  sizeof(*ptr) << endl; //! this give value without inisilizing the array
    // cout <<" size of address of pointer : " <<  sizeof(&ptr) << endl;
    // cout << " address of pointer : " << &ptr << endl;


//! 2 -> Symbol Table content cant be changed

    int arr[4] = {0,2,3,4};
    //arr = arr + 1; //? gives error bcs trying to change the symbol table values that assignes to this

    int *ptr = &arr[0];
    cout <<"adress value before increment : "<< ptr << endl;
    ptr += 1; //? it means pointer point to next index not changing the symbol table value
    cout << "adress value after increment : " << ptr << endl;
    cout << *(ptr + 1) << endl;

    return 0;
}