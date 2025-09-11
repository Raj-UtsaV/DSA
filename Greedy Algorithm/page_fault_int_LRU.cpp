#include <thread>
#include <chrono>
#include <iostream>
#include <vector>
#include <algorithm>
#include <list>
#include <unordered_map>
#include <string>

using namespace std;

class Solution
{
public:
    int pageFaults(int N, int C, vector<int> pages)
    {
        int count = 0;
        vector<int> v;
        for (int i = 0; i < N; i++)
        {
            auto it = find(v.begin(), v.end(), pages[i]);

            if (it == v.end())
            {

                // of the size is full
                if (v.size() == C)
                {
                    // remove LRU
                    v.erase(v.begin());
                }
                v.push_back(pages[i]);
                count++;
            }
            else
            {
                // SET RU
                v.erase(it);
                v.push_back(pages[i]);
            }
        }
        return count;
    }
};

class solution
{
public:
    int pageFaults(int N, int C, vector<int> pages)
    {
        list<int> cache;
        unordered_map<int, list<int>::iterator> mp;
        int count = 0;
        for (int i = 0; i < N; ++i)
        {
            int page = pages[i];
            if (mp.find(page) == mp.end())
            {
                count++;
                if (cache.size() == C)
                {
                    mp.erase(cache.front());
                    cache.pop_front();
                }
                cache.push_back(page);
                mp[page] = --cache.end();
            }
            else
            {
                cache.erase(mp[page]);
                cache.push_back(page);
                mp[page] = --cache.end();
            }
        }
        return count;
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
        vector<int> page{2, 3, 1, 3, 1, 3, 1, 2};
        int capacity = 3;
        Solution Sol;
        solution sol;
        cout << Sol.pageFaults(8, capacity, page) << endl;
        cout << sol.pageFaults(8, capacity, page) << endl;
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