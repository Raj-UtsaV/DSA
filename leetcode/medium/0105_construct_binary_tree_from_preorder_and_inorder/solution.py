"""Canonical solution metadata.

Problem Number: 105
Problem Title: Construct Binary Tree from Preorder and Inorder Traversal
Platform: LeetCode
Difficulty: Medium
Official Platform Topics: Array, Hash Table, Divide and Conquer, Tree, Binary Tree
Study Tags: Recursive Partitioning
Canonical URL: https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val, self.left, self.right = val, left, right

class Solution:
    def buildTree(self, preorder, inorder):
        positions={v:i for i,v in enumerate(inorder)}; pre=iter(preorder)
        def build(left,right):
            if left>right: return None
            root=TreeNode(next(pre)); mid=positions[root.val]
            root.left=build(left,mid-1); root.right=build(mid+1,right); return root
        return build(0,len(inorder)-1)
