"""Canonical solution metadata.

Problem Number: 543
Problem Title: Diameter of Binary Tree
Platform: LeetCode
Difficulty: Easy
Official Platform Topics: Tree, Depth-First Search, Binary Tree, DP on Trees
Study Tags: Tree DP
Canonical URL: https://leetcode.com/problems/diameter-of-binary-tree/
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val, self.left, self.right = val, left, right

class Solution:
    def diameterOfBinaryTree(self, root):
        answer=0
        def height(node):
            nonlocal answer
            if not node: return 0
            left,right=height(node.left),height(node.right); answer=max(answer,left+right); return 1+max(left,right)
        height(root); return answer
