#include<iostream>
#include<vector>

using namespace std;

void dfs(int node,vector<vector<int>> &adjLS, vector<int> &vis){
    vis[node] = 1;
    for(auto it:adjLS[node]){
        if(!vis[it]){
            dfs(it,adjLS,vis);
        }
    }
}

int numProvinces(vector<vector<int>> adj) {
    vector<vector<int>> adjLS(adj.size());
    for(int i=0;i<adj.size();i++){
        for(int j=0;j<adj.size();j++){
            if(adj[i][j] == 1 && i!=j){
                adjLS[i].push_back(j);
                adjLS[j].push_back(i);
            }
        }
    }

    vector<int> vis(adj.size(),0);
    int cnt=0;
    for(int i=0;i<adj.size();i++){
        if(!vis[i]){
            cnt++;
            dfs(i,adjLS,vis);
        }
    }
    
    return cnt;
}

int main(){
    vector<vector<int>> adj{{1,0,1},{0,1,0},{1,0,1}};
    cout<<numProvinces(adj);
    return 0;
}
