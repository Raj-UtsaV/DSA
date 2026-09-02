"""Canonical solution metadata.

Problem Number: 106
Problem Title: Construct Binary Tree from Inorder and Postorder Traversal
Platform: LeetCode
Difficulty: Medium
Official Platform Topics: Array, Hash Table, Divide and Conquer, Tree, Binary Tree
Study Tags: Recursive Partitioning
Canonical URL: https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val, self.left, self.right = val, left, right

class Solution:
    def buildTree(self, inorder, postorder):
        positions={v:i for i,v in enumerate(inorder)}
        def build(left,right):
            if left>right: return None
            root=TreeNode(postorder.pop()); mid=positions[root.val]
            root.right=build(mid+1,right); root.left=build(left,mid-1); return root
        return build(0,len(inorder)-1)
