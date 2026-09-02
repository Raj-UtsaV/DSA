"""Canonical solution metadata.

Problem Number: 653
Problem Title: Two Sum IV - Input is a BST
Platform: LeetCode
Difficulty: Easy
Official Platform Topics: Hash Table, Two Pointers, Tree, Depth-First Search, Breadth-First Search, Binary Search Tree, Binary Tree
Study Tags: Complement Set
Canonical URL: https://leetcode.com/problems/two-sum-iv-input-is-a-bst/
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val, self.left, self.right = val, left, right

class Solution:
    def findTarget(self, root, k):
        seen=set(); stack=[root]
        while stack:
            node=stack.pop()
            if not node: continue
            if k-node.val in seen: return True
            seen.add(node.val); stack.extend((node.left,node.right))
        return False
