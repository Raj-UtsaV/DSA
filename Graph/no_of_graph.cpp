#include<iostream>
#include<math.h>

using namespace std;



long long graph(int n){
    long long x = n * (n-1)/2;

    long long res = 1;
    const int MOD = 1e9+7;
    long long y = 2;

    while(x>0){
        if(x&1) res =  (res * y) % MOD;
        y = (y*y) %MOD;
        x = x/2;
    }

    return res;
}

int main(){
    int n = 5;
    cout<<"No. of Undirected graph : "<<graph(n)<<endl;

    return 0;
}