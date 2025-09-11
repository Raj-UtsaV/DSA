//? https://www.hackerrank.com/challenges/cpp-maps/problem?isFullScreen=true

#include<iostream>
#include<map>
#define ll long long

using namespace std;

int main() {
    int t;
    cin >> t;
    map<string, int> m;
    while (t--) {
        int y;
        cin >> y;

        if (y == 1) {
            string s;
            int x;
            cin >> s >> x;
            auto it = m.find(s);
            if (it != m.end()) (*it).second = (*it).second + x;
            else m.insert({ s,x });
        }

        if (y == 2) {
            string s;
            cin >> s;
            m.erase(s);
        }

        if (y == 3) {
            string s;
            cin >> s;
            auto it = m.find(s);
            if (it != m.end()) {
                cout << (*it).second << endl;
            }
            else cout << "0\n";
        }
    }
    return 0;
}