#include <iostream>
#include <vector>
#include <stack>
#include <algorithm>
using namespace std;

class optimal
{
public:
    int max_area(vector<int> v)
    {
        stack<int> st;
        int max_area = 0;
        for (int i = 0; i < v.size(); i++)
        {
            while (!st.empty() && v[st.top()] >= v[i])
            {
                int element = st.top();
                st.pop();
                int pse = st.empty() ? -1 : st.top();
                int nse = i;
                max_area = max(max_area, v[element] * (nse - pse - 1));
            }
            st.push(i);
        }

        while (!st.empty())
        {

            int element = st.top();
            st.pop();
            int pse = st.empty() ? -1 : st.top();
            int nse = v.size();
            max_area = max(max_area, v[element] * (nse - pse - 1));
        }
        return max_area;
    }
};

vector<vector<char>> prefix_sum1(vector<vector<char>> matrix)
{
    int m = matrix.size();
    int n = matrix[0].size();
    vector<vector<char>> prefix_sum(m, vector<char>(n)); // Corrected dimensions

    for (int j = 0; j < m; j++)
    {
        int sum = 0;
        for (int i = 0; i < n; i++)
        {
            sum += matrix[j][i] - '0';
            if (matrix[j][i] == '0')
            {
                sum = 0;
            }
            prefix_sum[j][i] = sum + '0'; // Corrected char conversion
        }
    }

    return prefix_sum;
}
// int max_rectangle(vector<vector<char>> matrix)
int main()
{
    vector<vector<char>> matrix = {{'1', '0', '1', '0', '0'}, {'1', '0', '1', '1', '1'}, {'1', '1', '1', '1', '1'}, {'1', '0', '0', '1', '0'}};
    matrix = prefix_sum1(matrix);
    return 0;
}