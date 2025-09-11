#include<vector>
#include<limits.h>
#include<iostream>
#include<queue>
#include<utility>
#include<algorithm>
using namespace std;


vector<int> shortestPath( vector<pair<int,int>> edges , int n , int m, int s , int t){
    vector<vector<pair<int,int>>> adj(n+1);
    for(auto it:edges){
        int u = it.first;
        int v = it.second;

        adj[u].push_back({1,v});
        adj[v].push_back({1,u});
    }

    priority_queue<pair<int,int>,vector<pair<int,int>>,greater<pair<int,int>>> pq;
    vector<int> dist(n+1,INT_MAX);
    vector<int> parent(n+1);
    pq.push({0,s});
    dist[s] = 0;
    parent[s] = -1;

    while(!pq.empty()){
        auto[dis,node] = pq.top();
        pq.pop();
        for(auto neigh : adj[node]){
            auto[ewt,adjnode] = neigh;
            if(dis + ewt < dist[adjnode]){
                dist[adjnode] = dis + ewt;
                parent[adjnode] = node;
                pq.push({dist[adjnode],adjnode});
            }
        }
    }

    vector<int> path(n+1);
    if(dist[t] == INT_MAX) return {};

    int current  = t;
    while(current != s){
        path.push_back(current);
        current = parent[current];
    }
    path.push_back(s);
    reverse(path.begin(),path.end());

    return path;
}
        
  