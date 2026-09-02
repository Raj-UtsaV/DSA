"""Canonical solution metadata.

Problem Number: 987
Problem Title: Vertical Order Traversal of a Binary Tree
Platform: LeetCode
Difficulty: Hard
Official Platform Topics: Hash Table, Tree, Depth-First Search, Breadth-First Search, Sorting, Binary Tree
Study Tags: Coordinate Ordering
Canonical URL: https://leetcode.com/problems/vertical-order-traversal-of-a-binary-tree/
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val, self.left, self.right = val, left, right

class Solution:
    def verticalTraversal(self, root):
        nodes=[]
        def walk(node,row,col):
            if node: nodes.append((col,row,node.val)); walk(node.left,row+1,col-1); walk(node.right,row+1,col+1)
        walk(root,0,0); nodes.sort(); answer=[]; previous=None
        for col,row,value in nodes:
            if col!=previous: answer.append([]); previous=col
            answer[-1].append(value)
        return answer
