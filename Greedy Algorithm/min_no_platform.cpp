#include <thread>
#include <chrono>
#include <iostream>
#include <vector>
#include <algorithm>
#include <string>

using namespace std;

int min_platform(vector<int> arr, vector<int> dep)
{
    int max_platform = 0;
    for (int i = 0; i < arr.size(); i++)
    {
        int cnt = 1;
        for (int j = i + 1; j < arr.size(); j++)
        {
            if ((arr[i] >= arr[j] && arr[i] <= dep[j]) ||
                (arr[j] >= arr[i] && arr[j] <= dep[i]))
            {
                cnt++;
            }
        }
        max_platform = max(max_platform, cnt);
    }
    return max_platform;
}

int by_time(vector<int> arr, vector<int>dep){
    sort(arr.begin(), arr.end());
    sort(dep.begin(), dep.end());
    int i,j,cnt,max_platform;
    i=j=cnt=max_platform=0;
    while(i<arr.size() && j<dep.size()){
        if(arr[i]<=dep[j]){
            i++;
            cnt++;
        }
        else{
            j++;
            cnt--;
        }
        max_platform = max(max_platform, cnt);
    }
    return max_platform;
}

int main()
{
    std::chrono::time_point<std::chrono::high_resolution_clock> starttime;
    {
        system("cls");
        starttime = std::chrono::high_resolution_clock::now();
    }

    // todo In this block write your code
    {
        vector<int> arr{900, 1235, 1100};
        vector<int> dep{1000, 1240, 1200};
        cout << "Minimum number of platforms required: " << min_platform(arr, dep) << endl;
        cout << "Minimum number of platforms required: " << by_time(arr, dep) << endl;
    }

    {
        auto endtime = std::chrono::high_resolution_clock::now();
        auto duration = std::chrono::duration_cast<std::chrono::microseconds>(endtime - starttime).count();
        std::cout << std::endl;
        std::cout << "Execution time: " << duration / 1000000.0 << " seconds" << std::endl;
        std::this_thread::sleep_for(std::chrono::seconds(10));
        system("cls");
    }
    return 0;
}