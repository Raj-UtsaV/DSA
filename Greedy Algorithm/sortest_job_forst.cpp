// scheduling policy that selects sortest waiting process with the smallest execution time to execute next
//


#include <thread>
#include <chrono>
#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
 
using namespace std;


class Solution {
  public:
    long long solve(vector<int>& bt) {
        sort(bt.begin(), bt.end());
        long long time_taken = 0, waiting_time = 0;
        for(int i = 0; i < bt.size(); i++) {
            waiting_time += time_taken;
            time_taken += bt[i];
        }
        return waiting_time/bt.size();
    }
};
 
int main() {
    std::chrono::time_point<std::chrono::high_resolution_clock> starttime;
   {
        system("cls");
        starttime = std::chrono::high_resolution_clock::now();
   }
 
   //todo In this block write your code
   {
        vector<int> jobs{4,3,7,1,2};
        Solution sol;
        cout<<sol.solve(jobs)<<endl;
   }
 
   {
        auto endtime = std::chrono::high_resolution_clock::now();
        auto duration = std::chrono::duration_cast<std::chrono::microseconds>(endtime - starttime).count();
        std::cout <<std::endl;
        std::cout<< "Execution time: " << duration/1000000.0 << " seconds" << std::endl;
        std::this_thread::sleep_for(std::chrono::seconds(10));
        system("cls");
   }
    return 0;
}