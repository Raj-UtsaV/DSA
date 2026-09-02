"""Canonical solution metadata.

Problem Number: 199
Problem Title: Binary Tree Right Side View
Platform: LeetCode
Difficulty: Medium
Official Platform Topics: Tree, Depth-First Search, Breadth-First Search, Binary Tree
Study Tags: Right-First Traversal
Canonical URL: https://leetcode.com/problems/binary-tree-right-side-view/
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val, self.left, self.right = val, left, right

class Solution:
    def rightSideView(self, root):
        answer=[]
        def visit(node,depth):
            if not node: return
            if depth==len(answer): answer.append(node.val)
            visit(node.right,depth+1); visit(node.left,depth+1)
        visit(root,0); return answer
