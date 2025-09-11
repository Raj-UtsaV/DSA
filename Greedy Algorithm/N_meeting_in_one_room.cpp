#include <thread>
#include <chrono>
#include <iostream>
#include <vector>
#include <algorithm>
#include <string>

using namespace std;

int max_meeting(vector<int> start, vector<int> end)
{
    vector<pair<int, int>> meetings;
    for (int i = 0; i < start.size(); i++)
    {
        meetings.push_back({start[i], end[i]});
    }
    sort(meetings.begin(), meetings.end(), [](pair<int, int> &a, pair<int, int> &b)
         { return a.second < b.second; });

    int count = 1;
    int free_time = meetings[0].second;

    for (int i = 1; i < meetings.size(); i++)
    {
        if (meetings[i].first >= free_time)
        {
            count++;
            free_time = meetings[i].second;
        }
    }

    return count;
}

int main()
{
    std::chrono::time_point<std::chrono::high_resolution_clock> starttime;

    {
        system("cls");
        starttime = std::chrono::high_resolution_clock::now();
    }

    //? Code block where you can write your code
    {
        vector<int> start{1, 3, 0, 5, 8, 5};
        vector<int> end{2, 4, 6, 7, 9, 9};

        int maxMeetings = max_meeting(start, end);
        cout << "Maximum number of meetings: " << maxMeetings << endl;
    }

    {
        auto endtime = std::chrono::high_resolution_clock::now();
        auto duration = std::chrono::duration_cast<std::chrono::microseconds>(endtime - starttime).count();
        cout << endl;
        cout << "Execution time: " << duration / 1000000.0 << " seconds" << endl;
        std::this_thread::sleep_for(std::chrono::seconds(10));
        system("cls");
    }

    return 0;
}
