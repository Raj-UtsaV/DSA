#include <iostream>
#include <vector>
using namespace std;

vector<int> brute(vector<int> v, int x, vector<int> indices)
{
    vector<int> ans;
    for (int i = 0; i < x; i++)
    {
        int y = indices[i];
        int cmp = v[y];
        int count = 0;
        for (int j = y + 1; j < v.size(); j++)
        {
            if (v[j] > cmp)
                count++;
        }

        ans.push_back(count);
    }

    return ans;
}

int main()
{
    vector<int> v = {3, 4, 2, 7, 5, 8, 10, 6};
    int queries = 2;
    vector<int> indices = {0, 5};
    vector<int> ans = brute(v, queries, indices);
    for (int i = 0; i < ans.size(); i++)
    {
        cout << ans[i] << " ";
    }

    return 0;
}