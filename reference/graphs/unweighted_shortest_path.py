"""Reusable reference: unweighted shortest paths."""

from collections import deque
def shortest_paths(adjacency,source):
 distance=[-1]*len(adjacency);distance[source]=0;queue=deque([source])
 while queue:
  node=queue.popleft()
  for neighbor in adjacency[node]:
   if distance[neighbor]<0:distance[neighbor]=distance[node]+1;queue.append(neighbor)
 return distance
