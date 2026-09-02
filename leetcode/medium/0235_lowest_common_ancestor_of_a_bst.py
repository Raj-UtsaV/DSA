"""Canonical solution metadata.

Problem Number: 235
Problem Title: Lowest Common Ancestor of a Binary Search Tree
Platform: LeetCode
Difficulty: Medium
Official Platform Topics: Tree, Depth-First Search, Binary Search Tree, Binary Tree, Binary Lifting, Lowest Common Ancestor
Study Tags: BST Ordering, LCA
Canonical URL: https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val, self.left, self.right = val, left, right

class Solution:
    def lowestCommonAncestor(self, root, p, q):
        low, high = sorted((p.val,q.val))
        while root:
            if root.val < low: root=root.right
            elif root.val > high: root=root.left
            else: return root
