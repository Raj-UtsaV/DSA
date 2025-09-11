#include <iostream>
using namespace std;


int brute(string s){
    int maxlen = 0;
    int size = s.length();
    for (int i = 0; i < size; i++)
    {
        int arr[256] = {0};
        for (int j = i; j < size; j++)
        {
            int x = int(s[j]);
            if (arr[x] == 1)
                break;
            int len = j - i + 1;
            maxlen = max(maxlen, len);
            arr[x] = 1;
        }
    }
    return maxlen;
}


int optimal(string s){
    int arr[256];
    fill(arr, arr + 256, -1);
    int n = s.length();
    int l = 0, r = 0;
    int maxlen = 0;

    while (r < n)
    {
        int x = static_cast<int>(s[r]);
        if (arr[x] != -1 && arr[x] >= l)
        {
            l = arr[x] + 1;
        }
        int len = r - l + 1;
        maxlen = max(maxlen, len);
        arr[x] = r;
        r++;
    }

    return maxlen;
}
 
int main() {
    string s = "abcabcbb";
    cout << brute(s) << endl; // output 3
    cout << optimal(s) << endl; // output 3
    return 0;
}