"""Reusable reference: binary-search-tree utilities."""

class TreeNode:
 def __init__(self,val):self.val=val;self.left=self.right=None
def insert(root,value):
 if not root:return TreeNode(value)
 if value<root.val:root.left=insert(root.left,value)
 elif value>root.val:root.right=insert(root.right,value)
 return root
def search(root,value):
 while root and root.val!=value:root=root.left if value<root.val else root.right
 return root
def delete(root,value):
 if not root:return None
 if value<root.val:root.left=delete(root.left,value)
 elif value>root.val:root.right=delete(root.right,value)
 else:
  if not root.left:return root.right
  if not root.right:return root.left
  successor=root.right
  while successor.left:successor=successor.left
  root.val=successor.val;root.right=delete(root.right,successor.val)
 return root
