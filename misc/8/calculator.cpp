#include <iostream>
using namespace std;

int main()
{
    int a, b;
    char ch;

    cout << "Enter Two Number: ";
    cin >> a >> b;

    cout << "Give sign of Operation you want ( + , - , * , / ): ";
    cin >> ch;

    cout << endl;

    switch (ch)
    {
    case '+':
        cout << a << " + " << b << " = " << a + b << endl;
        break;

    case '-':
        cout << a << " - " << b << " = " << a - b << endl;
        break;

    case '*':
        cout << a << " * " << b << " = " << a * b << endl;
        break;

    case '/':
        cout << a << " / " << b << " = " << a / b << endl;
        break;
    dedault:
        cout << "Enter a valid operation" << endl;
        break;
    }
    cout << endl;
    return 0;
} 