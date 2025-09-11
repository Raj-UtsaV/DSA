#include <iostream>
#include<map>
#include<algorithm>
using namespace std;

string better(int arr[],int k,int n){
    map<int, int> mpp;
    for (int i = 0; i < n;i++){
        int a = arr[i];
        int more = k - a;
        if(mpp.find(more) != mpp.end()){
            return "YES";
        }
        mpp[a] = i;
    }
    return "NO";
}
 
string best(int arr[],int n,int k){
    sort(arr, arr + n);
    int s = 0;
    int e = n-1;
    while(s<e){
        if(arr[s]+arr[e] == k)
            return "YES";
        else if(arr[s]+arr[e] < k)
            s++;
        else
            e--;
    }
    return "NO";
}

int main() {
    int arr[5] = {-2, -1, -3, -4};
    cout<<better(arr, -19, 5)<<endl;
    cout<<best(arr, -5, 5)<<endl;
    
    return 0;
}