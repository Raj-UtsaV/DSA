#include <iostream>
#include<math.h>
#include <cstdint>
using namespace std;

int nth_root(int n, int m)
{
    int s = 1;
    long long e = m / n;
    while(s<=e){
        long long mid = s + (e - s) / 2;
        long long val = pow(mid, n);
        cout << s << " " << mid << " " << e << " " << val << endl;
        if(val == m)
            return mid;
        else if (val < m && val != INT64_MIN)
            s = mid + 1;
        else 
            e = mid - 1;
    }
    return -1;
}

int main()
{
    int n, m;
    cin >> n >> m;
    cout << nth_root(n, m);
    return 0;
}