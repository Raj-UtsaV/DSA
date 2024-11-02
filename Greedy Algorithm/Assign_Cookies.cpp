#include <thread>
#include <chrono>
#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
 
//using namespace std;

int maxPossible(std::vector<int> children, std::vector<int> cookies) {

    sort(children.begin(), children.end());
    sort(cookies.begin(), cookies.end());

    int l = 0, r = 0;

    while (r < children.size() && l < cookies.size()) {
        if(children[r]<=cookies[l]){
            r++;
        }
        l++; // we always increase cookies bcs if current children not satisfied the surely the next children
             // will not satisft bcs of the sorted children array i.e greed factor  of next children will always be greater
    }

    return r;
}
 
int main() {
    std::chrono::time_point<std::chrono::high_resolution_clock> starttime;
   {
        system("cls");
        starttime = std::chrono::high_resolution_clock::now();
   }
 
   //todo In this block write your code
   {
        std::vector<int> children {1,2,3};
        std::vector<int> cookies{1,1};
        std::cout<<maxPossible(children,cookies)<<std::endl; //? expected 1
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