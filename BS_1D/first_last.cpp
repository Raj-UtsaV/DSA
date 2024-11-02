#include <iostream>
#include <algorithm>
using namespace std;

void f_l_brute(int arr[],int n,int x){
    int first = -1;
    int last = -1;
    for (int i = 0; i < n;i++){
        if(arr[i] == x){
            if(first == -1)
                first = i;
            last = i;
        }
    }
    cout << first << " " << last;
}

void f_l_best(int arr[],int n,int x){
    int s = 0;
    int e = n - 1;
    int ans = n;
    while(s<=e){
        int mid = s + (e - s) / 2;
        if(arr[mid] >= x){
            ans = mid;
            e = mid - 1;
        }
        else
            s = mid + 1;
    }
    if(ans == n || arr[ans] != x){
        cout << "-1 -1";
    }
    else{
        cout << ans << " ";

        s = 0;
        e = n - 1;
        ans = n;
        while(s<=e){
            int mid = s + (e - s) / 2;
            if (arr[mid] > x)
            {
                ans = mid;
                e = mid - 1;
            }
            else
                s = mid + 1;
        }
        cout << ans-1 << " ";
    }
}

void f_l_best_func(int *arr,int n,int x)
{
    int x1 = lower_bound(arr, arr + n, x) - arr;
    if(x1 == n || arr[x1]!=x){
        cout << "-1 -1";
    }
    else{
        cout << x1 << " ";
        x1 = upper_bound(arr, arr + n, x) - arr;
        cout << x1 - 1;
    }
}

void basic_code(int *arr,int n,int x){
    int first = -1;
    int second = -1;
    int s = 0;
    int e = n - 1;
    while(s<=e){
        int mid = s + (e - s) / 2;
        if(arr[mid] == x){
            first = mid;
            e = mid - 1;
        }
        else if(arr[mid] > x){
            e = mid - 1;
        }
        else
            s = mid + 1;
    }
    if(first == -1){
        cout << first << " " << second;
    }
    else {
        s = 0;
        e = n - 1;
        while(s<=e){
            int mid = s + (e - s) / 2;
            if (arr[mid] == x)
            {
                second = mid;
                s = mid + 1;
            }
            else if (arr[mid] > x)
            {
                e = mid - 1;
            }
            else
                s = mid + 1;
        }

        cout << first << " " <<second;
    }
}

int main() {
    int arr[5] = {1, 2, 2, 4, 4};
    f_l_brute(arr, 5, 2);
    cout << endl;
    f_l_best(arr, 5, 2);
    cout << endl;
    f_l_best_func(arr, 5, 2);
    cout << endl;
    basic_code(arr, 5, 2);
    return 0;
}