#include <thread>
#include <chrono>
#include <iostream>
#include<string>
#include<algorithm>

int brute(std::string s){
    int n =s.length();
    int maxsubstr = 0;
    for(int i=0;i<n;i++){
        int arr[3] = {0};
        for(int j=i;j<n;j++){
            arr[s[j]-'a']=1;
            if(arr[0]+arr[1]+arr[2] == 3){
                maxsubstr += n-j;
                break;
            }
        }
    }
    return maxsubstr;
}

int optimal(std::string s) {
    int maxsubstr = 0;
    int n = s.length();
    int arr[3];
    std::fill(arr,arr+3,-1);
    for (int i = 0; i < n; i++) {
        arr[s[i] - 'a'] = i;
        if (arr[0] != -1 && arr[1] != -1 && arr[2] != -1) {
            maxsubstr += *std::min_element(arr, arr + 3) +1;
        }
    }
    return maxsubstr;
}

 
int main() {
   {
        system("cls");
   }
 
   //! In this block write your code
   {
        std::string s = "abcabc";
        std::cout << brute(s) << std::endl; // output 10
        std::cout << optimal(s) << std::endl; // output 10
        
   }
 
   {
        std::this_thread::sleep_for(std::chrono::seconds(4));
        system("cls");
   }
    return 0;
}