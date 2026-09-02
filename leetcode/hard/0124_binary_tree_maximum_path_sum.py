"""Canonical solution metadata.

Problem Number: 124
Problem Title: Binary Tree Maximum Path Sum
Platform: LeetCode
Difficulty: Hard
Official Platform Topics: Dynamic Programming, Tree, Depth-First Search, Binary Tree, DP on Trees
Study Tags: Tree DP
Canonical URL: https://leetcode.com/problems/binary-tree-maximum-path-sum/
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val, self.left, self.right = val, left, right

class Solution:
    def maxPathSum(self, root):
        answer=float("-inf")
        def gain(node):
            nonlocal answer
            if not node: return 0
            left=max(0,gain(node.left)); right=max(0,gain(node.right)); answer=max(answer,node.val+left+right)
            return node.val+max(left,right)
        gain(root); return answer
