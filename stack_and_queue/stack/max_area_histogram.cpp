#include <iostream>
#include <vector>
#include <stack>
#include <algorithm>
using namespace std;

class brute
{
private:
    vector<int> find_NSEE(vector<int> v)
    {
        vector<int> res(v.size(), v.size());
        stack<int> s;

        for (int i = v.size() - 1; i >= 0; i--)
        {
            while (!s.empty() && v[s.top()] >= v[i])
            {
                s.pop();
            }
            if (!s.empty())
            {
                res[i] = s.top();
            }
            s.push(i);
        }
        return res;
    }

    vector<int> find_psee(vector<int> v)
    {
        vector<int> res(v.size(), -1);
        stack<int> s;

        for (int i = 0; i < v.size(); i++)
        {
            while (!s.empty() && v[s.top()] >= v[i])
            {
                s.pop();
            }
            if (!s.empty())
            {
                res[i] = s.top();
            }
            s.push(i);
        }
        return res;
    }

public:
    int find_area(vector<int> v)
    {
        vector<int> nse = find_NSEE(v);
        vector<int> pse = find_psee(v);
        int max_area = 0;
        for (int i = 0; i < v.size(); i++)
        {
            int area = (nse[i] - pse[i] - 1) * v[i];
            max_area = max(max_area, area);
        }
        return max_area;
    }
};

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
                int element = st.top(); st.pop();
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
            int pse = st.empty()? -1 : st.top();
            int nse = v.size();
            max_area = max(max_area, v[element] * (nse - pse - 1));
        }
        return max_area;
    }
};

int main()
{
    vector<int> v = {1, 2};
    brute br;
    cout << "Maximum area is " << br.find_area(v) << endl;

    optimal op;
    cout << "Maximum area is " << op.max_area(v) << endl;
    return 0;
}
