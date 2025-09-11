#include <iostream>
using namespace std;
 
int main() {
    int arr[6] = {7, 1, 5, 3, 6, 4};
    int mini = arr[0];
    int profit = 0;

    for (auto i:arr){
        int cost = i - mini;
        profit = max(profit, cost);
        mini = min(mini, i);
    }

    cout << profit;
    return 0;
}