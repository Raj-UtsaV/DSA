#include <thread>
#include <chrono>
#include <iostream>
#include <vector>
#include <algorithm>
#include <string>

using namespace std;

bool possible_to_sell(vector<int> bills)
{
    int five = 0;
    int ten = 0;
    for (int i = 0; i < bills.size(); i++)
    {
        if (bills[i] == 5)
            five++;
        else if (bills[i] == 10)
        {
            if (five)
            {
                ten++;
                five--;
            }
            else
                return false;
        }
        else
        {
            if (ten && five)
            {
                ten--;
                five--;
            }
            else if (five >= 3)
            {
                five -= 3;
            }
            else
                return false;
        }
    }
    return true;
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
        vector<int> bills{5,5,5,10,20};
        cout << possible_to_sell(bills) << endl;
    }

    {
        auto endtime = std::chrono::high_resolution_clock::now();
        auto duration = std::chrono::duration_cast<std::chrono::microseconds>(endtime - starttime).count();
        std::cout << std::endl;
        std::cout << "Execution time: " << duration / 1000000.0 << " seconds" << std::endl;
        std::this_thread::sleep_for(std::chrono::seconds(4));
        //system("cls");
    }
    return 0;
}