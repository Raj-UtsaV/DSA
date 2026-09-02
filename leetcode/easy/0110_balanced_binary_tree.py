"""Canonical solution metadata.

Problem Number: 110
Problem Title: Balanced Binary Tree
Platform: LeetCode
Difficulty: Easy
Official Platform Topics: Tree, Depth-First Search, Binary Tree
Study Tags: Postorder Height
Canonical URL: https://leetcode.com/problems/balanced-binary-tree/
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val, self.left, self.right = val, left, right

class Solution:
    def isBalanced(self, root):
        def height(node):
            if not node: return 0
            left=height(node.left); right=height(node.right)
            return -1 if left<0 or right<0 or abs(left-right)>1 else 1+max(left,right)
        return height(root)>=0
