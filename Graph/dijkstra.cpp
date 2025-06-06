#include <queue>
#include<vector>
#include<limits.h> 
#include<iostream>
#include<set>
using namespace std;

vector<int> dijkstra1(vector<vector<int>> &vec, int vertices, int edges, int source) {
    // Write your code here.

    vector<vector<pair<int,int>>> adj(vertices);
    for(auto it:vec){
        int u = it[0];
        int v = it[1];
        int wt = it[2];
        adj[u].push_back({v,wt});
        adj[v].push_back({u,wt});
    }

    priority_queue<pair<int,int>,vector<pair<int,int>>,greater<pair<int,int>>> pq;
    vector<int> dist(vertices,INT_MAX);
    dist[source] = 0;
    pq.push({0,source});

    while(!pq.empty()){
        auto[dis,node] = pq.top();
        pq.pop();

        for(auto it:adj[node]){
            auto[adjnode,ewt] = it;
            
            if(dis + ewt < dist[adjnode]){
                dist[adjnode] = dis + ewt;
                pq.push({dist[adjnode],adjnode});
            }
        }

    }

    return dist;

}

vector<int> dijkstra2(vector<vector<int>> &vec, int vertices, int edges, int source){
    vector<vector<pair<int,int>>> adj(vertices);
    for(auto it:vec){
        int u = it[0];
        int v = it[1];
        int wt = it[2];
        adj[u].push_back({v,wt});
        adj[v].push_back({u,wt});
    }

    set<pair<int,int>> st;
    vector<int> dist(vertices,INT_MAX);
    dist[source] = 0;
    st.insert({0,source});

    while(!st.empty()){
        auto it = *(st.begin());
        auto[dis,node] = it;
        st.erase(it);

        for(auto neigh:adj[node]){
            auto[adjnode,ewt] = neigh;
            if(dis+ewt < dist[adjnode]) {
                if(dist[adjnode] != INT_MAX) st.erase({dist[adjnode],adjnode});
                dist[adjnode] = dis + ewt;
                st.insert({dist[adjnode],adjnode});
            }
        }
    }

    return dist;
}



int main() {
    int V = 5, E = 6;
    vector<vector<int>> edges = {
        {0,1,2},
        {0,2,4},
        {1,2,1},
        {1,3,7},
        {2,4,3},
        {3,4,1}
    };
    int source = 0;
    vector<int> shortestDistances = dijkstra2(edges, V, E, source);
    for (int d : shortestDistances) cout << d << " ";
}
