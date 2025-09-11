#include <iostream>
using namespace std;
 
int main() {
    int arr[] = {-2,1,-3,4,-1,2,1,-5,4};
    int sum = 0;
    int maxi = INT_MIN;
    for(auto i:arr){
        sum += i;
        maxi = max(sum, maxi);
        if(sum<0)
            sum = 0;
    }
    cout << maxi;
    return 0;
}