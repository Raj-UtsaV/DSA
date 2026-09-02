"""Reusable reference: Dijkstra shortest paths."""

from heapq import heappop,heappush
def dijkstra(adjacency,source):
 distance={node:float('inf') for node in adjacency};distance[source]=0;heap=[(0,source)]
 while heap:
  dist,node=heappop(heap)
  if dist!=distance[node]:continue
  for neighbor,weight in adjacency[node]:
   candidate=dist+weight
   if candidate<distance[neighbor]:distance[neighbor]=candidate;heappush(heap,(candidate,neighbor))
 return distance
