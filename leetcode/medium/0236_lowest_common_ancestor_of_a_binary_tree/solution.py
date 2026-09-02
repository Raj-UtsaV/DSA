"""Canonical solution metadata.

Problem Number: 236
Problem Title: Lowest Common Ancestor of a Binary Tree
Platform: LeetCode
Difficulty: Medium
Official Platform Topics: Tree, Depth-First Search, Binary Tree, Binary Lifting, Lowest Common Ancestor
Study Tags: Postorder Recursion, LCA
Canonical URL: https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val, self.left, self.right = val, left, right

class Solution:
    def lowestCommonAncestor(self, root, p, q):
        if not root or root is p or root is q: return root
        left=self.lowestCommonAncestor(root.left,p,q); right=self.lowestCommonAncestor(root.right,p,q)
        return root if left and right else left or right
