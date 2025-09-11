#include <thread>
#include <chrono>
#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
 
using namespace std;

int min_jump(vector<int> nums,int index = 0,int jumps = 0){
     if(index >= nums.size()-1) return jumps;
     int mini = INT_MAX;
     for(int i=1;i<=nums[index];i++){
          mini= min(mini,min_jump(nums,index+i,jumps+1)); // trying all possible index where it can able to jump from current index
     }
     return mini;
}

int optimal(vector<int> nums){
     int jumps = 0, r =0,l=0;
     while(r<nums.size()-1){
          int farthest=0;    // taking range max where i can      jump
          for(int i=l;i<=r;i++){
               farthest = max(farthest,i+nums[i]);
          }
          l=r+1;
          r=farthest;
          jumps++;
     }
     return jumps;
}
 
int main() {
    std::chrono::time_point<std::chrono::high_resolution_clock> starttime;
   {
        system("cls");
        starttime = std::chrono::high_resolution_clock::now();
   }
 
   //todo In this block write your code
   {
        vector<int> nums{2,3,1,1,4};
        cout<<min_jump(nums)<<endl; //? Expected 2
        cout<<optimal(nums)<<endl; //? Expected 2
        
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