"""Canonical solution metadata.

Problem Number: Not applicable
Problem Title: Add 1 to a Number Represented as Linked List
Platform: GeeksforGeeks
Difficulty: Not reliably specified
Official Platform Topics: Not specified
Study Tags: Carry Propagation, Linked List
Canonical URL: https://www.geeksforgeeks.org/problems/add-1-to-a-number-represented-as-linked-list/1
"""

def add_one(head):
 def visit(node):
  if not node:return 1
  total=node.data+visit(node.next);node.data=total%10;return total//10
 carry=visit(head)
 if carry:
  node=type(head)(carry);node.next=head;return node
 return head
