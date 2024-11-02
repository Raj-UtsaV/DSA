#include <iostream>
#include <math.h>
using namespace std;

// int main(){
//     int n;
//     cin>>n;
//     int ans = 0;
//     int i = 0;
//     while(n != 0){
//         int bit= n&1;
//         ans=(bit * pow(10, i))+ ans;
//         n=n>>1;
//         i++;
//     }
//     cout<<ans<<endl;

//     return 0;
// }

// int main(){
//     int n,a,b;
//     cin>>n;
//     int ans=0;
//     int i=0;
//     a=~n;
//     b=a+1;
//     while(b != 0){
//         int bit= a&1;
//         ans=(bit * pow(10, i))+ ans;
//         b=b>>1;
//         i++;
//     }
//     cout<<ans<<endl;

//     return 0;
// }

int main()
{
    int n,m;
    cin >> n>>m;
    int ans = 0;
    int ans1=0;
    int i = 0;
    while (n != 0)
    {
        int digit = n % 10;
        if (digit == 1)
        {
            ans = ans + pow(2, i);
        }
        n = n / 10;
        i++;
    }
    while (m != 0)
    {
        int digit = m % 10;
        if (digit == 1)
        {
            ans1 = ans1 + pow(2, i);
        }
        m = m / 10;
        i++;
    }
    cout << ans <<" "<<ans1<< endl;
    return 0;
}