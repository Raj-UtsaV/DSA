"""Reusable reference: adjacency-list construction."""

def undirected_adjacency_list(vertices,edges):
 adjacency=[[] for _ in range(vertices)]
 for left,right in edges:adjacency[left].append(right);adjacency[right].append(left)
 return adjacency
