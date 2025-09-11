#include <iostream>
using namespace std;
int ans = 1;

int power()
{
    int a, b;
    cin >> a >> b;
    for (int i = 0; i < b; i++)
    {
        ans = ans * a;
    }
    return ans;
}

int main()
{
    int ans = power();
    cout << "answer is " << ans;

    int ans = power();
    cout << "answer is " << ans;
    
    int ans = power();
    cout << "answer is " << ans;

    return 0;
}