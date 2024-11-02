#include <iostream>
using namespace std;

// dunction signature

void counting(int a)
{

    // dunction body

    for (int i = 1; i <= a; i++)
    {
        cout << i << endl;
    }
}

int main()
{
    int num;
    cin >> num;
    cout << endl;

    // dunction call

    counting(num);

    return 0;
}