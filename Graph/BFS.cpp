#include <iostream>
#include <vector>
#include <queue>
using namespace std;

vector<int> bfsOfGraph(vector<vector<int>> &adj)
{
  vector<int> bfs;
  vector<bool> visited(adj.size(), false);
  queue<int> q;
  q.push(0);
  visited[0]=true;

  while (q.size())
  {
    auto node = q.front();
    q.pop();
    bfs.push_back(node);

    for (auto it : adj[node])
    {
      if (!visited[it])
      {
        visited[it] = true;
        q.push(it);
      }
    }
  }
  return bfs;
}

int main()
{
  vector<vector<int>> adj{{2, 3, 1}, {0}, {0, 4}, {0}, {2}};
  vector<int> result = bfsOfGraph(adj);
  for (int i = 0; i < result.size(); i++)
  {
    cout << result[i] << " ";
  }
  return 0;
}
