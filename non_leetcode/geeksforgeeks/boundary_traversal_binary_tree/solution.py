"""Canonical solution metadata.

Problem Number: Not applicable
Problem Title: Boundary Traversal of Binary Tree
Platform: GeeksforGeeks
Difficulty: Not reliably specified
Official Platform Topics: Not specified
Study Tags: Tree Traversal
Canonical URL: https://www.geeksforgeeks.org/problems/boundary-traversal-of-binary-tree/1
"""

def boundary(root):
 if not root:return []
 def leaf(n):return n and not n.left and not n.right
 out=[] if leaf(root) else [root.data];node=root.left
 while node:
  if not leaf(node):out.append(node.data)
  node=node.left or node.right
 def leaves(node):
  if not node:return
  if leaf(node):out.append(node.data);return
  leaves(node.left);leaves(node.right)
 leaves(root);right=[];node=root.right
 while node:
  if not leaf(node):right.append(node.data)
  node=node.right or node.left
 return out+right[::-1]
