#include<iostream>
#include <stack>
#include<vector>
using namespace std;

int brute(vector<int> arr){
    int n = arr.size();
    int waterTrapped = 0;
    for (int i = 0; i < n; i++)
    {
        int j = i;
        int leftMax = 0, rightMax = 0;
        while (j >= 0)
        {
            leftMax = max(leftMax, arr[j]);
            j--;
        }
        
        j = i;
        while (j < n)
        {
            rightMax = max(rightMax, arr[j]);
            j++;
        }
        waterTrapped += min(leftMax, rightMax) - arr[i];
    }
    return waterTrapped;
}

int better(vector<int> arr){
    int n = arr.size();
    int prefix[n], suffix[n];  //? to calculate left amx and right max of the blocks
    prefix[0] = arr[0];
    for (int i = 1; i < n; i++)
    {
        prefix[i] = max(prefix[i - 1], arr[i]);
    }
    suffix[n - 1] = arr[n - 1];
    for (int i = n - 2; i >= 0; i--)
    {
        suffix[i] = max(suffix[i + 1], arr[i]);
    }
    int waterTrapped = 0;
    for (int i = 0; i < n; i++)
    {
        waterTrapped += min(prefix[i], suffix[i]) - arr[i];
    }
    return waterTrapped;
}

int optimal(vector<int> arr){
    int leftmax = 0;
    int rightmax = 0;
    int total = 0;
    int s = 0;
    int e = arr.size() - 1;
    while(s<=e){
        if(arr[s]<=arr[e]){
            if(arr[s]>=leftmax) leftmax = arr[s];
            else
                total += leftmax - arr[s];
            s++;
        }
        else{
            if(arr[e]>=rightmax)
                rightmax = arr[e];
            else total+=rightmax - arr[e];
            e--;
        }
        
    }
    return total;
}

int main(){
    vector<int> height = {4,2,0,3,2,5};
    cout << brute(height)<<endl;
    cout << better(height)<<endl;
    cout << optimal(height)<<endl;
    return 0;
}