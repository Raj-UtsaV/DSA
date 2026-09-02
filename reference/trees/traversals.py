"""Reusable reference: binary-tree BFS and DFS traversals."""

from collections import deque
def preorder(root):return [] if not root else [root.val]+preorder(root.left)+preorder(root.right)
def inorder(root):return [] if not root else inorder(root.left)+[root.val]+inorder(root.right)
def postorder(root):return [] if not root else postorder(root.left)+postorder(root.right)+[root.val]
def level_order(root):
 if not root:return []
 queue=deque([root]);out=[]
 while queue:
  node=queue.popleft();out.append(node.val)
  if node.left:queue.append(node.left)
  if node.right:queue.append(node.right)
 return out
def root_to_node(root,target):
 path=[]
 def find(node):
  if not node:return False
  path.append(node.val)
  if node.val==target or find(node.left) or find(node.right):return True
  path.pop();return False
 return path if find(root) else []
