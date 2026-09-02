"""Canonical solution metadata.

Problem Number: 662
Problem Title: Maximum Width of Binary Tree
Platform: LeetCode
Difficulty: Medium
Official Platform Topics: Tree, Depth-First Search, Breadth-First Search, Binary Tree
Study Tags: Indexed Level Order
Canonical URL: https://leetcode.com/problems/maximum-width-of-binary-tree/
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val, self.left, self.right = val, left, right

from collections import deque
class Solution:
    def widthOfBinaryTree(self, root):
        if not root: return 0
        queue=deque([(root,0)]); answer=0
        while queue:
            base=queue[0][1]; answer=max(answer,queue[-1][1]-base+1)
            for _ in range(len(queue)):
                node,index=queue.popleft(); index-=base
                if node.left: queue.append((node.left,2*index))
                if node.right: queue.append((node.right,2*index+1))
        return answer
