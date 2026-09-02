"""Canonical solution metadata.

Problem Number: 114
Problem Title: Flatten Binary Tree to Linked List
Platform: LeetCode
Difficulty: Medium
Official Platform Topics: Linked List, Stack, Tree, Depth-First Search, Binary Tree
Study Tags: Preorder Rewiring
Canonical URL: https://leetcode.com/problems/flatten-binary-tree-to-linked-list/
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val, self.left, self.right = val, left, right

class Solution:
    def flatten(self, root):
        node=root
        while node:
            if node.left:
                predecessor=node.left
                while predecessor.right: predecessor=predecessor.right
                predecessor.right=node.right; node.right=node.left; node.left=None
            node=node.right
