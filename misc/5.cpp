#include<iostream>
using namespace std;

int main(){
    int a=5;
    int b=5;
    

    cout<<"a&b "<<(a&b)<<endl;
    cout<<"a|b "<<(a|b)<<endl;
    cout<<"~a "<<~a<<endl;
    cout<<"a^b "<<(a^b)<<endl;
    return 0;
}

//........ledt shidt(<<) & right shidt(>>).............
/*  #include<iostream>
//   using namespace std;
  
//   int main(){
//       cout<<(5<<1)<<endl;
//       cout<<(5>>1)<<endl;
      
//       return 0;
//   }*/

// //...............int/dec...............
// //   #include<iostream>
// //   using namespace std;
// //   
// //   int main(){
//     //   int i=5;
//     //   cout<<i++<<endl;
//      //  5 i=6
//     //   cout<<++i<<endl;
//      //  7 i=7
//     //   cout<<i--<<endl;
//       // 7 i=6
//     //   cout<<--i<<endl;
//       // 5 i=5
//     //   return 0;
// //   }

// //.........................for loop.......................
//  #include<iostream>
//  using namespace std;
 
//  int main(){
//     int n;
//     cin>>n;
//     // cout<<"printhing the number drom 1 to "<<n<<endl;
//     // for (int i = 1; i <= n; i++ )
//     // {
//     //     cout<<i<<endl;
//     // }
    
//     // return 0;


//   int sum=0;
//   for (int i = 0; i <= n; i++)
//   {
//     sum= sum+i;
//     //sum +=i;
//  }
//   cout<<sum<<endl;
//  }

#include <iostream>
using namespace std;
void repeat(int arr[], int size)
{
  int k;
  for (int j = 0; j < size; j++)
  {
    k = arr[j];

    int ans = 0;
    for (int i = 0; i < size; i++)
    {
      if (k == arr[i])
      {
        ans = ans + 1;
      }
    }
    if (ans == 1)
    {
      cout << k;
    }
  }
}

int main()
{
  int arr[5] = {1, 5, 3, 4, 5};
  repeat(arr, 5);
  return 0;
}