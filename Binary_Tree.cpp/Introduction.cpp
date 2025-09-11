#include <iostream>
#include <vector>
#include <algorithm>
#include <math.h>
#include <string>
using namespace std;

int countNodes_ith_same_level(int i){
    return pow(2,i-1);
}
 
int main() {
   {
        system("cls");
   }
 
   //todo In this block write your code
   {
        int i = 5;
        cout<<countNodes_ith_same_level(i)<<endl;
   }

    return 0;
}