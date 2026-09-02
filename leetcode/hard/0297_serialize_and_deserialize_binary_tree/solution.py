"""Canonical solution metadata.

Problem Number: 297
Problem Title: Serialize and Deserialize Binary Tree
Platform: LeetCode
Difficulty: Hard
Official Platform Topics: String, Tree, Depth-First Search, Breadth-First Search, Design, Binary Tree
Study Tags: Preorder Encoding
Canonical URL: https://leetcode.com/problems/serialize-and-deserialize-binary-tree/
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val, self.left, self.right = val, left, right

class Codec:
    def serialize(self, root):
        values=[]
        def walk(node):
            if not node: values.append("#"); return
            values.append(str(node.val)); walk(node.left); walk(node.right)
        walk(root); return ",".join(values)
    def deserialize(self, data):
        values=iter(data.split(","))
        def build():
            value=next(values)
            if value=="#": return None
            node=TreeNode(int(value)); node.left=build(); node.right=build(); return node
        return build()
