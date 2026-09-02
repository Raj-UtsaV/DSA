"""Reusable reference: binary-tree node and level-order construction."""

from collections import deque
class TreeNode:
 def __init__(self,val=0,left=None,right=None):self.val,self.left,self.right=val,left,right
def from_level_order(values,null=None):
 if not values or values[0]==null:return None
 root=TreeNode(values[0]);queue=deque([root]);i=1
 while queue and i<len(values):
  node=queue.popleft()
  if values[i]!=null:node.left=TreeNode(values[i]);queue.append(node.left)
  i+=1
  if i<len(values) and values[i]!=null:node.right=TreeNode(values[i]);queue.append(node.right)
  i+=1
 return root
