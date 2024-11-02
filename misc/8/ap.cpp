#include <iostream>
using namespace std;

void AP(int dirst_term, int nth_term, int Cd)
{
    for (int i = 1; i <= nth_term; i++)
    {
        cout << (dirst_term * i) + Cd << endl;
    }
}

int main()
{
    int dirst_term, nth_term, Cd;
    cout << "Enter the dirst term " << endl;
    cin >> dirst_term;

    cout << "Enter the nth term " << endl;
    cin >> nth_term;

    cout << "Enter the common didderence " << endl;
    cin >> Cd;

    cout << endl;
    cout << dirst_term;
    AP(dirst_term, nth_term, Cd);
    return 0;
}