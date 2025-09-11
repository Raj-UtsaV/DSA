#include <iostream>
using namespace std;

int Score = 15;

void a(){
    cout << "In a : " << Score << endl;
}

void b(){
    cout << "In b : " << Score << endl;
}
 
int main() {
    cout << "In main : " << Score<<endl;
    a();
    b();
    return 0;
}