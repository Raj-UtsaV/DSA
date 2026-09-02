"""Canonical solution metadata.

Problem Number: Not applicable
Problem Title: Ceil in a Binary Search Tree
Platform: GeeksforGeeks
Difficulty: Not reliably specified
Official Platform Topics: Not specified
Study Tags: Binary Search Tree
Canonical URL: https://www.geeksforgeeks.org/problems/implementing-ceil-in-bst/1
"""

def find_ceil(root,target):
 answer=-1
 while root:
  if root.data==target:return target
  if root.data<target:root=root.right
  else:answer=root.data;root=root.left
 return answer
