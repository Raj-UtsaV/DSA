"""Canonical solution metadata.

Problem Number: 1008
Problem Title: Construct Binary Search Tree from Preorder Traversal
Platform: LeetCode
Difficulty: Medium
Official Platform Topics: Array, Stack, Tree, Binary Search Tree, Monotonic Stack, Binary Tree
Study Tags: Bounded Recursion
Canonical URL: https://leetcode.com/problems/construct-binary-search-tree-from-preorder-traversal/
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val, self.left, self.right = val, left, right

class Solution:
    def bstFromPreorder(self, preorder):
        index = 0
        def build(bound):
            nonlocal index
            if index == len(preorder) or preorder[index] > bound: return None
            root = TreeNode(preorder[index]); index += 1
            root.left = build(root.val); root.right = build(bound); return root
        return build(float("inf"))
