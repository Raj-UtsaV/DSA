"""Reusable reference: depth-first graph traversal."""

def dfs(adjacency,start=0):
 seen=set();order=[]
 def visit(node):
  seen.add(node);order.append(node)
  for neighbor in adjacency[node]:
   if neighbor not in seen:visit(neighbor)
 visit(start);return order
