#include <iostream>
#include<map>
#include<set>
#include<utility>
#include<vector>


using namespace std;
 
// int main() {
//     map<pair<string, string>, vector<int>> m;

//     int n;
//     cin >> n;

//     for (int i = 0;i < n;i++) {
//         string fn, ln;
//         int ct;
//         cin >> fn >> ln >> ct;

//         for (int i = 0;i < ct;i++) {
//             int x;
//             cin >> x;
//             m[{fn, ln}].push_back(x);
//         }
//     }


//     for (auto &pr : m) {
//         auto &full_name = pr.first;
//         auto& list = pr.second;

//         cout << full_name.first << " " << full_name.second << " " << list.size();

//     }
    

//     return 0;
// }


int main() {
    map<int, multiset<string>> m;

    int n;
    cin >> n;

    for (int i = 0;i < n;i++) {
        int mark;
        string name;
        cin >> mark >> name;
        m[mark].insert(name);
    }

    auto cur_it = --m.end();

    while (true) {
        auto &students = (*cur_it).second;
        int marks = (*cur_it).first;
        for (auto student : students) {
            cout << student << " " << marks << endl;
        }

        if (cur_it == m.begin()) break;
        cur_it--;
        
    }

    return 0;


}