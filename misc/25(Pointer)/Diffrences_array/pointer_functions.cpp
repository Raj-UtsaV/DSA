#include <iostream>
using namespace std;

auto update(auto *p){
    *p = *p + 1;

}

auto sum(auto arr[],auto n){
    cout << "Size : " << sizeof(arr) << endl;

    auto sum1 = 0;
    for (int i = 0; i < n;i++)
    {
        sum1 += i[arr];
    }

    return sum1;
}
 
int main() {
    auto val = 5;
    auto *p = &val;
    cout << "Before : " << *p << endl;

    update(p);

    cout << "After : " << *p << endl;

    int arr[5] = {1,2,3,4,5};
    cout << "Sum is : " << sum(arr + 3, 2) << endl;
    return 0;
}