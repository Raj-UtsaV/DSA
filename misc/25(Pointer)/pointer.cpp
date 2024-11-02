#include <iostream>
using namespace std;
 
int main() {
    int num = 5,num1 = 6;
    auto *ptr = &num,*ptr1 = &num1;

    //! Basics of pointer 
    cout << "The Valur stored in the address stored in ptr : "<<*ptr<<endl;
    cout << "The address stored in ptr : "<<ptr<<endl;
    cout << "size of ptr : "<<sizeof(ptr)<<endl;
    cout << "size of integer: "<<sizeof(num)<<endl<<endl;

    //! Pointer Operations
    cout << "Before Increment : " << *ptr + *ptr1 << endl;
    (*ptr)++;
    cout <<"After Increment : "<<*ptr + *ptr1<<endl<<endl;

    //! copying pointer
    auto *ptr2 = ptr;
    cout << ptr2 << "-" << ptr<<endl;
    cout << *ptr2 << "-" << *ptr<<endl;

    return 0;
}