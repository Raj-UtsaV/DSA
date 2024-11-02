//---------------------------PAttern-------------------

// #include<iostream>
// using namespace std;

// int main(){
//     int n;
//     cin>>n;

//     int i=1;
//     int a=1;
//     while(i<=n){
//         int j=1;
//         while(j<=n){
//             cout<<a<<" ";
//             a=a+1;
//             j=j+1;
//         }
//         cout<<endl;
//         i=i+1;
//     }
//     return 0;
// }

// #include<iostream>
// using namespace std;

// int main(){
//     int n;
//     cin>>n;
//     int i=1;
//     while(i<=n){
//         int j=1;
//         while(j<=i){
//             cout<<"*";
//             j=j+1;
//         }
//         cout<<endl;
//         i=i+1;
//     }
//     return 0;
// }

// #include<iostream>
// using namespace std;

// int main(){
//     int n;
//     cin>>n;
//     int row=1;
//     while(row<=n){
//         int col=1;
//         while(col<=row){
//             cout<<row;
//             col=col+1;
//         }
//         cout<<endl;
//         row=row+1;
//     }
//     return 0;
// }


#include<iostream>
using namespace std;

int main(){
    int n;
    cin>>n;
    int row=1;
    int a=row;

    while(row<=n){

        int col=1;
        while(col<=row){
            cout<<a;
            a=a+1;
            col=col+1;
        }
        cout<<endl;
        row=row+1;
    }
    return 0;
}


// #include<iostream>
// using namespace std;

// int main(){
//     int n;
//     cin>>n;
//     int row=1;

//     while(row<=n){

//         int col=1;
//         int a=row;
//         while(col<=row){
//             cout<<a;
//             a=a+1;
//             col=col+1;
//         }
//         cout<<endl;
//         row=row+1;
//     }
//     return 0;
// }

// #include<iostream>
// using namespace std;

// int main(){
//     int n;
//     cin>>n;
//     int row=1;

//     while(row<=n){

//         int col=1;
//         int a=row;
//         while(col<=row){
//             cout<<a;
//             a=a-1;
//             col=col+1;
//         }
//         cout<<endl;
//         row=row+1;
//     }
//     return 0;
// }

// #include <iostream>
// using namespace std;

// int main()
// {
//     int n;
//     cin >> n;
//     int row = 1;

//     while (row <= n)
//     {
//         int col = 1;

//         while (col <= n)
//         {
//             char p = 'A' + row - 1;
//             cout << p;
//             p = p + 1;
//             col = col + 1;
//         }
//         cout << endl;
//         row = row + 1;
//     }
//     return 0;
// }

// #include<iostream>
// using namespace std;

// int main(){
//     int n;
//     cin>>n;
//     int row=1;

//     while(row<=n){
//         int col=1;
//         while(col<=n){
//             char p='A'+col-1;
//             cout<<p;
//             p=p=1;
//             col=col+1;
//         }
//         cout<<endl;
//         row=row+1;

//     }
//     return 0;
// }

// #include<iostream>
// using namespace std;

// int main(){
//     int n;
//     cin>>n;
//     int row=1;
//     char p='A';
//     while(row<=n){
//         int col=1;
//         while(col<=n){

//             cout<<p;
//             p=p+1;
//             col=col+1;
//         }
//         cout<<endl;
//         row=row+1;
//     }

//     return 0;
// }

// #include<iostream>
// using namespace std;

// int main(){
//     int n;
//     cin>>n;
//     int row=1;

//     while(row<=n){
//         int col=1;
//         char p='A'+row+col-2;
//         while(col<=n){

//             cout<<p;
//             p=p+1;
//             col=col+1;
//         }
//         cout<<endl;
//         row=row+1;
//     }

//     return 0;
// }

// #include<iostream>
// using namespace std;

// int main(){
//     int n;
//     cin>>n;
//     int row=1;

//     while(row<=n){
//         int col=1;
//         char p='A'+row+col-2;
//         while(col<=n){

//             cout<<p;
//             p=p+1;
//             col=col+1;
//         }
//         cout<<endl;
//         row=row+1;
//     }

//     return 0;
// }

// #include<iostream>
// using namespace std;

// int main(){
//     int n;
//     cin>>n;
//     int row=1;
//     while (row<=n)
//     {
//         int col=1;
//         char ch='A';
//         while (col<=n)
//         {
//             cout<<ch;

//             col=col+1;

//         }
//         cout<<endl;
//         row=row+1;

//     }

//     return 0;
// }

