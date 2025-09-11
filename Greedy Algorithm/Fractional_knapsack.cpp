#include <thread>
#include <chrono>
#include <iostream>
#include <vector>
#include <algorithm>
#include <utility>

using namespace std;

vector<pair<int, int>> Pair(vector<int> values, vector<int> values_weight) {
    vector<pair<int, int>> pairs;
    for (int i = 0; i < values.size(); ++i) {
        pairs.push_back(make_pair(values[i], values_weight[i]));
    }
    // Sort pairs based on value/weight ratio in descending order
    sort(pairs.begin(), pairs.end(), [](pair<int, int> &a, pair<int, int> &b) {
        return double(a.first) / a.second > double(b.first) / b.second;
    });
    return pairs;
}

int main() {
    std::chrono::time_point<std::chrono::high_resolution_clock> starttime;

    {
        system("cls");
        starttime = std::chrono::high_resolution_clock::now();
    }

    // Code block where you can write your code
    {
        vector<int> values{60, 100, 120};
        vector<int> value_weight{10, 20, 30};
        vector<pair<int, int>> pairs = Pair(values, value_weight);
        int capacity = 50;
        int currweight = 0;
        double finalans = 0.0;

        for (int i = 0; i < pairs.size(); i++) {
            if (currweight + pairs[i].second <= capacity) {
                currweight += pairs[i].second;
                finalans += double(pairs[i].first);
            } else {
                int rem = capacity - currweight;
                finalans += double(pairs[i].first) / pairs[i].second * rem;
                break;
            }
        }

        cout << "Maximum value: " << finalans << endl;
    }

    {
        auto endtime = std::chrono::high_resolution_clock::now();
        auto duration = std::chrono::duration_cast<std::chrono::microseconds>(endtime - starttime).count();
        cout << endl;
        cout << "Execution time: " << duration / 1000000.0 << " seconds" << endl;
        std::this_thread::sleep_for(std::chrono::seconds(4));
        system("cls");
    }

    return 0;
}
