#include <thread>
#include <chrono>
#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
 
using namespace std;

class Solution {
public:
    vector<vector<int>> merge(vector<vector<int>>& intervals) {

        sort(intervals.begin(), intervals.end());

        vector<vector<int>> result;
        vector<int> temp_interval = intervals[0];

        for(int i = 1; i < intervals.size();i++){
            if(intervals[i][0] >  temp_interval[1] ){
                result.push_back(temp_interval);
                temp_interval = intervals[i];
            }
            else{
                temp_interval[1] = max(temp_interval[1], intervals[i][1]);
                temp_interval[0] = min(temp_interval[0], intervals[i][0]);
            }
        }
        result.push_back(temp_interval);
        return result;  
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
        vector<vector<int>> intervals{{1,2},{2,3},{3,4},{1,3}};
        Solution sol;
        vector<vector<int>> ans = sol.merge(intervals);
        for(auto interval : ans){
            cout << "[" << interval[0] << ", " << interval[1] << "]" << " ";
        }
        cout << endl;
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