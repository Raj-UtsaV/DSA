#include <thread>
#include <chrono>
#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
 
using namespace std;


bool can_reach(vector<int> nums){
    int max_jump = 0;
    for(int i=0; i<nums.size();i++){
        if(i>max_jump) return false;
        max_jump = max(max_jump, i+nums[i]);
        cout<<max_jump<<" ";
    }
    cout<<endl;
    return true;
}

bool can_reach_2(vector<int> nums){
    for(int i=nums.size()-1;i>=0;i++){
       
    }
    return true;
}
 
int main() {
    std::chrono::time_point<std::chrono::high_resolution_clock> starttime;
   {
        system("cls");
        starttime = std::chrono::high_resolution_clock::now();
   }
 
   //todo In this block write your code
   {
        vector<int> nums{3,2,1,0,4};
        cout<<can_reach(nums)<<endl;
        //cout<<can_reach_2(nums)<<endl;
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