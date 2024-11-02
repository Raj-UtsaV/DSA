// #include <iostream>
// using namespace std;
// bool find(int *arr, int n, int x)
// {
//     int s = 0;
//     int e = n - 1;
//     while (s <= e)
//     {
//         int mid = s + (e - s) / 2;
//         if (arr[mid] == x)
//             return true;
//         if (arr[s] == arr[mid] && arr[e] == arr[mid])
//         {
//             s = s + 1;
//             e = e - 1;
//             continue;
//         }

//         else if (arr[s] <= arr[mid])
//         {
//             if (arr[s] <= x && arr[mid] >= x)
//             {
//                 e = mid - 1;
//             }
//             else
//                 s = mid + 1;
//         }
//         else
//         {
//             if (arr[mid] <= x && arr[e] >= x)
//             {
//                 s = mid + 1;
//             }
//             else
//                 e = mid - 1;
//         }
//     }
//     return false;
// }

// int main()
// {
//     int arr[5] = {1, 0, 1, 1, 1};
//     cout << find(arr, 5, 0);

//     return 0;
// }

#include <iostream>
using namespace std;

//? Function to find an element x in a sorted array arr of size n
bool find(int *arr, int n, int x)
{
    //? Initialize start and end indices
    int s = 0;
    int e = n - 1;

    //? Binary search loop
    while (s <= e)
    {
        //? Calculate the middle index
        int mid = s + (e - s) / 2;

        //? If the middle element is equal to x, return true
        if (arr[mid] == x)
            return true;

        //? If the start and end elements are equal to the middle element,
        //? increment the start index and decrement the end index
        if (arr[s] == arr[mid] && arr[e] == arr[mid])
        {
            s = s + 1;
            e = e - 1;
            continue;
        }

        //? If the start element is less than or equal to the middle element,
        //? check if x is in the left half
        else if (arr[s] <= arr[mid])
        {
            //? If x is in the left half, update the end index
            if (arr[s] <= x && arr[mid] >= x)
            {
                e = mid - 1;
            }
            //? Otherwise, update the start index
            else
                s = mid + 1;
        }

        //? If the middle element is less than or equal to the end element,
        //? check if x is in the right half
        else
        {
            //? If x is in the right half, update the start index
            if (arr[mid] <= x && arr[e] >= x)
            {
                s = mid + 1;
            }
            //? Otherwise, update the end index
            else
                e = mid - 1;
        }
    }

    //? If x is not found, return false
    return false;
}

int main()
{
    //? Example array and target value
    int arr[5] = {1, 0, 1, 1, 1};
    cout << find(arr, 5, 0);

    return 0;
}