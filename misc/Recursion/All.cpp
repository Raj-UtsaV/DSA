#include <iostream>
#define ll long long
using namespace std;

ll int factorial(int n){
    if(n==0)
        return 1;

    return  n * factorial(n - 1);
    
}

ll int powof2(int n){
    if(n == 0)
        return 1;

    return 2 * powof2(n - 1);
}

void counting(int n){
    if(n == 0)
        return;

    
    counting(n - 1);
    cout << n << " ";
}

ll int fib(int n){
    if(n == 0)
        return 0;
    
    if(n==1)
        return 1;

    return fib(n - 1) + fib(n - 2);
    
}

int climbstair(int n){
    //!  Count Ways To Reach The N-th Stairs
    //!  https://www.naukri.com/code360/problems/count-ways-to-reach-nth-stairs_798650?count=25&page=1&search=&sort_entity=order&sort_order=ASC

    if(n<0)
        return 0;
    if(n==0)
        return 1;

    return climbstair(n - 1) + climbstair(n - 2);
}

void sayDigit(int n,string arr[]){

    //? base case
    if(n == 0)
        return;

    //? processing
    int digit = n % 10;
    n /= 10;
    

    //? recursive call
    sayDigit(n, arr);

    cout << digit[arr] << " ";
}

int main() {

    string arr[10] = {"zeor", "one", "two", "three", "four", "five", "siz", "seven", "eight", "nine"};
    int n;
    cout << "Enter n : ";
    cin >> n;

    cout << "Factorial is : "<< factorial(n)<<endl;
    cout << "Power of 2 is : " << powof2(n) << endl;
    cout << "Counting is : ";
    counting(n);
    cout << endl;
    cout << "nth term of Fibonnacci series is : " << fib(n) << endl;
    cout << "No. of ways to reach top by climbing n stairs : " << climbstair(n) << endl; 
    cout << endl;
    cout << "SayDigit : ";
    sayDigit(n, arr);
    cout << endl;

    return 0;
}