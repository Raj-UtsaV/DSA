//? https://www.hackerrank.com/challenges/cpp-sets/problem?isFullScreen=true

#include<iostream>
#include<set>

 
using namespace std;
 
int main(){
    int t;
    cin >> t;
    set<int> s;
    while (t--) {
        int n;
        cin >> n;

        if (n == 1) {
            int x;
            cin >> x;
            s.insert(x);
        }


        if (n == 2) {
            int x;
            cin >> x;
            s.erase(x);
        }


        if (n == 3) {
            int x;
            cin >> x;
            auto it = s.find(x);
            if (it != s.end()) cout << "YES\n";
            else cout << "NO\n";
        }

    }
return 0;
}