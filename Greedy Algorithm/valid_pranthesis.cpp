#include <thread>
#include <chrono>
#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
 
using namespace std;

bool recursive(string s,int index = 0,int count = 0){
    if(count<0) return 0;
    if(index==s.length()) return count==0;
    if(s[index] == '(') return recursive(s,index+1,count+1);
    if(s[index] == ')') return recursive(s,index+1,count-1);
    //todo if there id * the we have to replace it with ( or ) or " " accordingly the we will find ans 
    //todo any of this combination is correct then we return true else we return false
    return recursive(s,index+1,count+1) || recursive(s,index+1,count-1) || recursive(s,index+1,count);
}


bool optimal(string s){
    int min = 0;
    int max = 0;
    for(int i=0;i<s.size();i++){
        if(max < 0) return false;
        if(s[i] == '('){
            min++;
            max++;
        }
        else if(s[i] == ')'){
            min--;
            max--;
        }
        else{
            max++;  //? when "* " appear there should be only two conditions
                    //? it may be ( or ) if ( then max will inc if ) then min will decreaase
            if (min<0) min = 0;
    }
    return min==0;
}
 
int main() {
    std::chrono::time_point<std::chrono::high_resolution_clock> starttime;
   {
        system("cls");
        starttime = std::chrono::high_resolution_clock::now();
   }
 
   //todo In this block write your code
   {
        string s ="(*))";
        cout<<recursive(s)<<endl;
        cout<<optimal(s)<<endl;
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