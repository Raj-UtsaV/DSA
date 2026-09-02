"""Canonical solution metadata.

Problem Number: 230
Problem Title: Kth Smallest Element in a BST
Platform: LeetCode
Difficulty: Medium
Official Platform Topics: Tree, Depth-First Search, Binary Search Tree, Binary Tree
Study Tags: Inorder Traversal
Canonical URL: https://leetcode.com/problems/kth-smallest-element-in-a-bst/
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val, self.left, self.right = val, left, right

class Solution:
    def kthSmallest(self, root, k):
        stack=[]
        while True:
            while root: stack.append(root); root=root.left
            root=stack.pop(); k-=1
            if k==0: return root.val
            root=root.right
