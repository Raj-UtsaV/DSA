#include <iostream>
using namespace std;

// 1 --> prime no
// 0 --> not a prime no

bool isPrime(int a)
{

    for (int i = 2; i < a; i++)
    {
        if (a % i == 0)
        {
            return 0;
        }
        return 1;
    }
    if(a==2 ){
        return 1;
    }
}

int main()
{
    int num, b ;
    cin >> num;

    b = isPrime(num);
    if (b == 1)
    {
        cout << "The given number is prime";
    }
    else
    {
        cout << "The given number is not prime";
    }
    return 0;
}