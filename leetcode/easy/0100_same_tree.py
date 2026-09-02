"""Canonical solution metadata.

Problem Number: 100
Problem Title: Same Tree
Platform: LeetCode
Difficulty: Easy
Official Platform Topics: Tree, Depth-First Search, Breadth-First Search, Binary Tree
Study Tags: Paired Traversal
Canonical URL: https://leetcode.com/problems/same-tree/
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val, self.left, self.right = val, left, right

class Solution:
    def isSameTree(self, p, q):
        return p is q if not p or not q else p.val==q.val and self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right)
