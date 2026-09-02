"""Canonical solution metadata.

Problem Number: Not applicable
Problem Title: Remove Duplicates from Sorted Doubly Linked List
Platform: GeeksforGeeks
Difficulty: Not reliably specified
Official Platform Topics: Not specified
Study Tags: Doubly Linked List
Canonical URL: https://www.geeksforgeeks.org/problems/remove-duplicates-from-a-sorted-doubly-linked-list/1
"""

def remove_duplicates(head):
 node=head
 while node and node.next:
  if node.data==node.next.data:
   node.next=node.next.next
   if node.next:node.next.prev=node
  else:node=node.next
 return head
