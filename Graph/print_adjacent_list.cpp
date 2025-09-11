#include <iostream>
#include <vector>

using namespace std;

void store_matrix(int e, vector<pair<int, int>> &edges, vector<vector<int>> &matrix)
{
    for (int i = 0; i < e; i++)
    {
        int u = edges[i].first;
        int v = edges[i].second;

        matrix[u][v] = 1;
        matrix[v][u] = 1;
    }
}

void print_matrix(const vector<vector<int>> &matrix)
{
    for (const auto &row : matrix)
    {
        for (int val : row)
        {
            cout << val << " ";
        }
        cout << endl;
    }
}

void adj_list(int e, vector<pair<int ,int>> &edges,vector<vector<int>>&adj_List){
    for(int i=0;i<e;i++){
        int u = edges[i].first;
        int v = edges[i].second;

        adj_List[u].push_back(v);
        adj_List[v].push_back(u);
    }
}

int main()
{
    int n = 5, e = 7;
    vector<pair<int, int>> edges{{0, 1}, {0, 4}, {4, 1}, {4, 3}, {1, 3}, {1, 2}, {3, 2}};

    vector<vector<int>> matrix(n + 1, vector<int>(e + 1, 0));
    store_matrix(e, edges, matrix);
    //print_matrix(matrix);

    vector<vector<int>> adj_List(e+1);
    adj_list(e,edges,adj_List);
    print_matrix(adj_List);

}