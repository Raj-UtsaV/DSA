//?  find unique string using set

// #include <iostream>
// #include<set>
// using namespace std;

// int main() {

//     //!*  declaration
//     set<string> s;
//     int n;
//     cin >> n;
//     for (int i = 0;i < n;i++) {
//         string s1;
//         cin >> s1;

//         //*  to take iput
//         s.insert(s1);
//     }

//     //*  print
//     for (auto pr : s) {
//         cout << pr;
//         cout << endl;
//     }
//     return 0;
// }


//? Monk and the magical candy bag


// #include<iostream>
// #include<set>


// using namespace std;

// int main(){
//     int t;
//     cin>>t;
//     while (t--) {
//         int n, k;
//         cin >> n >> k;
//         long int count = 0;
//         multiset<long int> s;
//         for (int i = 0;i < n;i++) {
//             long int p;
//             cin >> p;
//             s.insert(p);
//         }

//         for (int i = 0;i < k;i++) {
//             auto it = --s.end();
//             long int p = *it;
//             count += p;
//             s.erase(it);
//             s.insert(p / 2);

//         }
//         cout << count << "\n";

//     }

// return 0;
// }



#include<iostream>
#include<set>
#include<utility>
#define ll long long
typedef pair<int, int> pairs;

using namespace std;

int main(){
    int t;
    cin>>t;
    while(t--){

        set<pairs> s;

        for (int i = 0;i < t;i++) {
            int  x, y;
            cin >> x >> y;
            pairs p1 = make_pair(x, y);
            s.insert(p1);
        }


    }
return 0;
}



