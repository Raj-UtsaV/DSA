"""Canonical solution metadata.

Problem Number: 285
Problem Title: Inorder Successor in BST
Platform: LeetCode
Difficulty: Medium
Official Platform Topics: Tree, Depth-First Search, Binary Search Tree, Binary Tree
Study Tags: Candidate Tracking
Canonical URL: https://leetcode.com/problems/inorder-successor-in-bst/
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val, self.left, self.right = val, left, right

class Solution:
    def inorderSuccessor(self, root, p):
        successor=None
        while root:
            if p.val < root.val: successor=root; root=root.left
            else: root=root.right
        return successor
