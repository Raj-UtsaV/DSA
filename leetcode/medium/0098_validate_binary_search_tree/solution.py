"""Canonical solution metadata.

Problem Number: 98
Problem Title: Validate Binary Search Tree
Platform: LeetCode
Difficulty: Medium
Official Platform Topics: Tree, Depth-First Search, Binary Search Tree, Binary Tree
Study Tags: Range Validation
Canonical URL: https://leetcode.com/problems/validate-binary-search-tree/
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val, self.left, self.right = val, left, right

class Solution:
    def isValidBST(self, root):
        def valid(node,low,high):
            return not node or low < node.val < high and valid(node.left,low,node.val) and valid(node.right,node.val,high)
        return valid(root,float("-inf"),float("inf"))
