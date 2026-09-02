"""Canonical solution metadata.

Problem Number: Not applicable
Problem Title: Top View of Binary Tree
Platform: GeeksforGeeks
Difficulty: Not reliably specified
Official Platform Topics: Not specified
Study Tags: Breadth-First Search, Horizontal Distance
Canonical URL: https://www.geeksforgeeks.org/problems/top-view-of-binary-tree/1
"""

from collections import deque
def top_view(root):
 if not root:return []
 view={};q=deque([(root,0)])
 while q:
  node,x=q.popleft();view.setdefault(x,node.data)
  if node.left:q.append((node.left,x-1))
  if node.right:q.append((node.right,x+1))
 return [view[x] for x in sorted(view)]
