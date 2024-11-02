#include <iostream>
using namespace std;

int main()
{
    int n, b = 1, a = 0;
    cin >> n;
    cout << a << " " << b << " ";
    for (int i = 1; i <= n; i++)
    {
        int nextNumber = a + b;
        cout << nextNumber << " ";
        a = b;
        b = nextNumber;
    }
    

    return 0;
}

// int main(){
//     int n;
//     cin>>n;
//     bool isprime=1;

//     for (int i = 2; i < n; i++)
//     {
//         if (n%i == 0){
//             isprime=0;
//             break;

//     }
//     if(isprime==0){
//         cout<<" not prime";
//     }
//     else{
//         cout<<"prime";
//     }

// }}