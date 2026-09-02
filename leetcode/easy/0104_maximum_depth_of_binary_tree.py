"""Canonical solution metadata.

Problem Number: 104
Problem Title: Maximum Depth of Binary Tree
Platform: LeetCode
Difficulty: Easy
Official Platform Topics: Tree, Depth-First Search, Breadth-First Search, Binary Tree
Study Tags: Tree Height
Canonical URL: https://leetcode.com/problems/maximum-depth-of-binary-tree/
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val, self.left, self.right = val, left, right

class Solution:
    def maxDepth(self, root): return 0 if not root else 1+max(self.maxDepth(root.left),self.maxDepth(root.right))
