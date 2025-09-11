#include <iostream>
using namespace std;

int main()
{
    int arr[5] = {4, 5, 1, 2, 3};
    int s = 0;
    int e = 4;
    int target = 1;
    while (s <= e)
    {
        int mid = s + (e - s) / 2;
        if (arr[mid] == target)
        {
            cout << mid;
            break;
        }

        //? left sorted?
        if(arr[s]<=arr[mid]){

            //todo checking if the element exist in the part s-mid
            if(arr[s]<=target && arr[mid]>=target)
                e = mid - 1;
            else
                s = mid + 1;
        }

        else{
            if(arr[mid] <=target && arr[e] >=target){
                s = mid + 1;
            }
            else
                e = mid - 1;
        }
    }
    return 0;
}