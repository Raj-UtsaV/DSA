"""Reusable reference: breadth-first graph traversal."""

from collections import deque
def bfs(adjacency,start=0):
 seen={start};queue=deque([start]);order=[]
 while queue:
  node=queue.popleft();order.append(node)
  for neighbor in adjacency[node]:
   if neighbor not in seen:seen.add(neighbor);queue.append(neighbor)
 return order
