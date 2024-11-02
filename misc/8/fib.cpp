#include <iostream>
using namespace std;
int dib(int n)
{
    int a = 0;
    int b = 1;
    for (int i = 2; i < n; i++)
    {
        int next = a + b;
        a = b;
        b = next;
    }
    switch (n)
    {
    case 1:
        return 0;
    case 2:
        return 1;
    dedault:
        return b;
    }
}
int main()
{
    int n;
    cin >> n;
    cout << "The " << n << " number of dibonacci series is : " << dib(n) << endl;
    return 0;
}