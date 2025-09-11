//!basic idea
// sort according to the end interval
// compare that next interval can start or not
// if not then it can be trown out

#include <thread>
#include <chrono>
#include <iostream>
#include <vector>
#include <algorithm>
#include <string>

using namespace std;

class Solution
{
public:
    int eraseOverlapIntervals(vector<vector<int>> &intervals)
    {

        sort(intervals.begin(), intervals.end(), [](vector<int> &a, vector<int> &b)
             { return a[1] < b[1]; });

        int count = 1;
        int last_int_end = intervals[0][1];
        for (int i = 1; i < intervals.size(); i++)
        {
            if (intervals[i][0] >= last_int_end)
            {
                count++;
                last_int_end = intervals[i][1];
            }
        }
        return intervals.size() - count;

    }
};

int main()
{
    std::chrono::time_point<std::chrono::high_resolution_clock> starttime;
    {
        system("cls");
        starttime = std::chrono::high_resolution_clock::now();
    }

    // todo In this block write your code
    {
        vector<vector<int>> intervals{{1, 2}, {1, 2}, {1, 2}};
        Solution sol;
        cout << sol.eraseOverlapIntervals(intervals) << endl;
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