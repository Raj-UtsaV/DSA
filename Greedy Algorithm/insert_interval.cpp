//! basic idea
// here we split given interval into 3 parts
// 1-> left part which is smaller than the overlapping
// 2-> overlapping part
// 3-> right part which is greater than the overlapping
// then we combine all of them together

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
    vector<vector<int>> insert(vector<vector<int>> &intervals, vector<int> &newInterval)
    {
        vector<vector<int>> result;
        int i = 0;

        //? left most part
        while (i < intervals.size() && intervals[i][1] < newInterval[0] ) 
        {
            result.push_back(intervals[i]);
            i++;
        }

        //? overlapping part
        while (i < intervals.size() && intervals[i][0] <= newInterval[1]) 
        {
            newInterval[0] = min(newInterval[0], intervals[i][0]);
            newInterval[1] = max(newInterval[1], intervals[i][1]);
            i++;
        }
        result.push_back(newInterval);

        //? right most part
        while (i < intervals.size())
        {
            result.push_back(intervals[i]);
            i++;
        }

        return result;
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
        vector<vector<int>> intervals{{1, 3}, {6, 9}};
        vector<int> new_interval{2, 5};
        Solution sol;
        vector<vector<int>> result = sol.insert(intervals, new_interval);
        for (auto &i : result)
        {
            cout << "[" << i[0] << ", " << i[1] << "]" << " ";
        }
        cout << endl;
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