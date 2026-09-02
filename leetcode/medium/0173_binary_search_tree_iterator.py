"""Canonical solution metadata.

Problem Number: 173
Problem Title: Binary Search Tree Iterator
Platform: LeetCode
Difficulty: Medium
Official Platform Topics: Stack, Tree, Design, Binary Search Tree, Binary Tree, Iterator
Study Tags: Lazy Inorder Traversal
Canonical URL: https://leetcode.com/problems/binary-search-tree-iterator/
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val, self.left, self.right = val, left, right

class BSTIterator:
    def __init__(self, root): self.stack=[]; self._push_left(root)
    def _push_left(self,node):
        while node: self.stack.append(node); node=node.left
    def next(self):
        node=self.stack.pop(); self._push_left(node.right); return node.val
    def hasNext(self): return bool(self.stack)
