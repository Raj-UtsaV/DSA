#include < iostream>
using namespace std;

int binarySearch(int a)
{
    int ans = 0;
    int s = 0;
    int e = a;
    int mid = s + (e - s) / 2;
    while (s <= e)
    {
        int square = mid * mid;

        if(square == a)
        {
            return mid;
        }
        if(square > a)
        {
            e = mid - 1;
        }

        if(square < a)
        {
            ans = mid;
            s = mid + 1;
        }
        mid = s + (e - s) / 2;
    }
    return ans;
}

double precision(int a, int prec, int tempsol)
{
    double dactor = 1;
    double ans = tempsol;
    for(int i = 0; i < prec; i++)
    {
        dactor = dactor / 10;
        for(double j = ans; j * j < a; j = j + dactor)
        {
            ans = j;
        }
    }
    return ans;
}

int main()
{
    int a;
    cin >> a;
    int tempsol = binarySearch(a);
    cout << precision(a, 4, tempsol);
    return 0;
}