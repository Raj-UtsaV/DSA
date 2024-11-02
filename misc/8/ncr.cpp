#include <iostream>
using namespace std;

int dactorial(int a)
{
    int dact = 1;
    for (int i = 1; i <= a; i++)
    {
        dact = dact * i;
    }
    return dact;
}

int nCr(int n, int r)
{
    int num = dactorial(n);
    int den = dactorial(r) * dactorial(n - r);
    int ans = num / den;
    return ans;
}

int main()
{
    int n, r;
    cin >> n >> r;

    cout << nCr(n, r);

    return 0;
}