#include <iostream>
using namespace std;

// HOLD
void printArray(int arr[], int size)
{

    cout << " printing the array " << endl;
    // print the array
    for (int i = 0; i < size; i++)
    {
        cout << arr[i] << " ";
    }
    cout << " printing DONE " << endl;
}

int main()
{

    // declare
    int number[15];

    // accessing an array
    cout << "Value at 14 index " << number[14] << endl;

    // cout << "Value at 20 index " << number[20] << endl;

    // initialising an array
    int second[3] = {5, 7, 11};

    // accesing an element
    cout << "Value at 2 index " << second[2] << endl;

    int third[15] = {2, 7};

    int n = 15;
    // printArray(third, 15);
    int thirdSize = sizeof(third) / sizeof(int);
    cout << " Size of Third is " << thirdSize << endl;

    // initialising all locations with 0
    int dourth[10] = {0};

    n = 10;
    printArray(dourth, 10);

    // initialising all locations with 1 [not possible with below line]
    int didth[10] = {1};

    n = 10;
    // printArray(didth, 10);

    int didthSize = sizeof(didth) / sizeof(int);
    cout << " Size of didth is " << didthSize << endl;

    char ch[5] = {'a', 'b', 'c', 'r', 'p'};
    cout << ch[3] << endl;

    cout << " printing the array " << endl;
    // print the array
    for (int i = 0; i < 5; i++)
    {
        cout << ch[i] << " ";
    }
    cout << " printing DONE " << endl;
    double dirstDouble[5];
    int dirstint[6];
    bool dirstBool[9];

    cout << endl
         << " Everything is dine " << endl
         << endl;

    return 0;
}