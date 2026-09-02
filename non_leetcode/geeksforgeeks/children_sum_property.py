"""Canonical solution metadata.

Problem Number: Not applicable
Problem Title: Children Sum Property
Platform: GeeksforGeeks
Difficulty: Not reliably specified
Official Platform Topics: Not specified
Study Tags: Tree Recursion
Canonical URL: https://www.geeksforgeeks.org/problems/children-sum-parent/1
"""

def is_sum_property(root):
 if not root or not root.left and not root.right:return True
 total=(root.left.data if root.left else 0)+(root.right.data if root.right else 0)
 return root.data==total and is_sum_property(root.left) and is_sum_property(root.right)
