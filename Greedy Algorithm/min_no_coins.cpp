#include <thread>
#include <chrono>
#include <iostream>
#include <vector>


 
using namespace std;

int coinChange(vector<int>& coins, int amount) {
    int count  = 0;
    for(int i=0;i<coins.size();i++){
        if(amount == 0) return count;
        if(coins[i]<=amount) {
            count += amount/coins[i];
            amount  =  amount%coins[i];
            cout<<count<<" "<<amount<<endl;
        }
    }
    if(amount == 0) return count;
    return -1;
}
 
int main() {
    std::chrono::time_point<std::chrono::high_resolution_clock> starttime;
   {
        system("cls");
        starttime = std::chrono::high_resolution_clock::now();
   }
 
   //todo In this block write your code
   { 
        vector<int> coins{9, 6, 5, 1};
        int target = 11;
        int ans = coinChange(coins, target);
        cout << ans << endl; // output 2

   }
 
   {
        auto endtime = std::chrono::high_resolution_clock::now();
        auto duration = std::chrono::duration_cast<std::chrono::microseconds>(endtime - starttime).count();
        std::cout <<std::endl;
        std::cout<< "Execution time: " << duration/1000000.0 << " seconds" << std::endl;
        std::this_thread::sleep_for(std::chrono::seconds(4));
        system("cls");
   }
    return 0;
}