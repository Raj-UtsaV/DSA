#include <iostream>
using namespace std;
 
int main() {
    int arr[5] = {1, 2, 3, 4, 5};
    char ch[6] = "abcde"; //? need extra space for null charcater

    cout << "print address of first index : " << arr << endl;
    cout << "Print Entire content of array : " << ch << endl;

    auto *c = &ch[0];
    //? Print entire atring intead of first index address
    cout << c << endl;

    char temp = 'z';
    auto *p = &temp;
    cout << p << endl;


    return 0;
}