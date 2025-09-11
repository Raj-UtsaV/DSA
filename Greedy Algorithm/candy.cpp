#include <thread>
#include <chrono>
#include <iostream>
#include <vector>
#include <algorithm>
#include<numeric>
#include <string>
 
using namespace std;

class minCandy {
public:
    int brute(vector<int> ratings) {
        int n = ratings.size();
        vector<int> candy(n, 1); // Each child must get at least one candy initially

        // Forward pass
        for (int i = 1; i < n; i++) {
            if (ratings[i] > ratings[i - 1]) {
                candy[i] = candy[i - 1] + 1;
            }
        }

        // Backward pass
        for (int i = n - 2; i >= 0; i--) {
            if (ratings[i] > ratings[i + 1]) {
                candy[i] = max(candy[i], candy[i + 1] + 1);
            }
        }

        return accumulate(candy.begin(), candy.end(), 0);
    }


    int optimized(vector<int> ratings) {
        int n = ratings.size();
        int sum = 1;
        int i=1;
        while(i<n){
          if(ratings[i] ==  ratings[i-1]){
               sum++;
               i++;
               continue;
          }

          int peak =1;
          while(i<n && ratings[i] > ratings[i-1]){
              peak++;
              sum += peak;
              i++;
          }

          int down = 1;
          while(i<n && ratings[i-1]> ratings[i]){
               sum+=down;
               i++;
               down++;
          }

          if(down > peak){
               sum+=down-peak;
          }
        }
        return sum;
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
        minCandy cnd;
        vector<int> v{1,2,2};
        cout<<cnd.brute(v)<<endl;
        cout<<cnd.optimized(v)<<endl;
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