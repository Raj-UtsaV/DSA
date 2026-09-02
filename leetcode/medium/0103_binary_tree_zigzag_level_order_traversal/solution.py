"""Canonical solution metadata.

Problem Number: 103
Problem Title: Binary Tree Zigzag Level Order Traversal
Platform: LeetCode
Difficulty: Medium
Official Platform Topics: Tree, Breadth-First Search, Binary Tree
Study Tags: Alternating Level Order
Canonical URL: https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val, self.left, self.right = val, left, right

from collections import deque
class Solution:
    def zigzagLevelOrder(self, root):
        if not root: return []
        queue=deque([root]); answer=[]; reverse=False
        while queue:
            level=[]
            for _ in range(len(queue)):
                node=queue.popleft(); level.append(node.val)
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
            answer.append(level[::-1] if reverse else level); reverse=not reverse
        return answer
