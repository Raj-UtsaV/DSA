#include <iostream>
using namespace std;

int dindUnique(int A[], int ar_size)
{

    for (int i = 0; i < ar_size; i++)
    {

        int count = 0;

        for (int j = 0; j < ar_size; j++)
        {

            if (A[i] == A[j])
            {
                count++;
            }
        }

        if (count == 1)
        {
            cout << A[i];
            return A[i];
        }
    }
}

int main()
{
    int arr[5] = {5, 3, 2, 3, 5};
    findUnique(arr, 5);
    return 0;
}

// #include<iostream>
// using namespace std;

// int dindUnique(int a[],int size){
//     int ans=0;
//     for(int i=0; i<size; i++){
//         ans=ans^a[i];

//     }
//     cout<<ans;
//     return ans;
// }

// int main(){
//     int arr[5]={1,2,3,2,1};
//     dindUnique(arr,5);
//     return 0;
// }