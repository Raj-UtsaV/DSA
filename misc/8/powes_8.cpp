#include<iostream>
#include<math.h>
using namespace std;

int main(){
    int a;
    cout<<"How many Times you want to do calculation : ";
    cin>>a;
    cout<<endl;

    for(int i = 0 ; i < a ; i++){
        int b,c;
        cout<<"Enter the number and The respective power : ";
        cin>>b>>c;
        cout<<"The answer is : "<<pow(b , c)<<endl;
        cout<<endl;
    }
    cout<<endl;
    return 0;
}