//! basic idea
// we want to maxmise the profit so we first sort the given array according to max profit
// after that we create a array of size last day to finish any job 
// assigned initailly with  -1 showing not any job not done already on that day
// we then assign the task to do at the deadline day and change the array value form -1 to jobid
// agar job sone array me already joib id hai to usse phle jiss day me -1 hoga uss din usko krenge

#include <thread>
#include <chrono>
#include <iostream>
#include <vector>
#include <algorithm>
#include <numeric>
#include <string>

using namespace std;

class Job
{
public:
     int jobid;
     int deadline;
     int profit;

     Job(int j, int d, int p) : jobid(j), deadline(d), profit(p) {}
};

vector<int> Jobs(vector<Job> jobs)
{
     int n = jobs.size();
     sort(jobs.begin(), jobs.end(), [](Job a, Job b)
          { return a.profit > b.profit; });

     int max_profit, cnt, last_day;
     max_profit = cnt = last_day = 0;

     for (int i = 0; i < n; i++)
     {
          last_day = max(last_day, jobs[i].deadline);
     }

     //? Create a vector to store the day when each job is assigned.
     vector<int> jobday(last_day + 1, -1);
     for (int i = 0; i < n; i++)
     {
          for (int j = jobs[i].deadline; j > 0; j--)
          {
               if (jobday[j] == -1)
               {
                    jobday[j] = jobs[i].jobid;
                    cnt++;
                    max_profit += jobs[i].profit;
                    break;
               }
          }
     }
     return {cnt, max_profit};
}

int main()
{
     std::chrono::time_point<std::chrono::high_resolution_clock> starttime;

     {
          system("cls");
          starttime = std::chrono::high_resolution_clock::now();
     }

     // Code block where you can write your code
     {
          vector<Job> jobs{{1, 4, 20}, {2, 1, 1}, {3, 1, 40}, {4, 1, 30}};
          vector<int> ans = Jobs(jobs);
          cout << "Number of Jobs assigned: " << ans[0] << endl;
          cout << "Maximum Profit: " << ans[1] << endl;
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
