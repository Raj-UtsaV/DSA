#include <iostream>
#include <vector>


using namespace std;

void dfs(int node,vector<vector<int>>&adj,vector<bool>&vis,vector<int>&ls){
    vis[node] = true;
    ls.push_back(node);

    for(auto it:adj[node]){
        if(!vis[it]) dfs(it,adj,vis,ls);
    }
}

vector<int> dfsOfGraph(vector<vector<int>> &adj)
{
    vector<bool> vis(adj.size(),false);
    int start = 0;
    vector<int> ls;
    dfs(start,adj,vis,ls);
    return ls;
}

int main()
{
    vector<vector<int>> adj{{2, 3, 1}, {0}, {0, 4}, {0}, {2}};
    vector<int> ls  = dfsOfGraph(adj);
    for(auto it:ls){
       cout<<it<<" "; 
    }
    return 0;
}
