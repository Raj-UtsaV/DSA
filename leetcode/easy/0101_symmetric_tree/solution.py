"""Canonical solution metadata.

Problem Number: 101
Problem Title: Symmetric Tree
Platform: LeetCode
Difficulty: Easy
Official Platform Topics: Tree, Depth-First Search, Breadth-First Search, Binary Tree
Study Tags: Mirror Traversal
Canonical URL: https://leetcode.com/problems/symmetric-tree/
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val, self.left, self.right = val, left, right

class Solution:
    def isSymmetric(self, root):
        def mirror(a,b): return a is b if not a or not b else a.val==b.val and mirror(a.left,b.right) and mirror(a.right,b.left)
        return mirror(root.left,root.right) if root else True
