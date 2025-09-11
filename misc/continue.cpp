// #include<iostream>
// using namespace std;

// int main(){
//     int n;
//     cin>>n;
//     for (int i = 1; i <=n; i++)
//     {
//         cout<<"hi"<<endl;
//         cout<<"hey"<<endl;
//         continue;
//         cout<<"replay to krde"<<endl;
//     }
    
//     return 0;
// }




#include<iostream>
using namespace std;

int main(){
    for (int i = 0; i <15; i++)
    {
        for (int j=i; j<=15; j++)
        {
            cout<<i<<" "<<j<<endl;
        }
        
    }
    
    return 0;
}
// int main(){
//     for (int i = 0; i <=15; i+=2)
//     {
//         cout<<i<<" ";
//        if(i&1){
//         continue;
//        } 
//        i++;
//     }
    
//     return 0;
// }