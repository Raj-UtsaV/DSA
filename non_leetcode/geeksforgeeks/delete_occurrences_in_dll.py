"""Canonical solution metadata.

Problem Number: Not applicable
Problem Title: Delete All Occurrences of a Key in a Doubly Linked List
Platform: GeeksforGeeks
Difficulty: Not reliably specified
Official Platform Topics: Not specified
Study Tags: Doubly Linked List
Canonical URL: https://www.geeksforgeeks.org/problems/delete-all-occurrences-of-a-given-key-in-a-doubly-linked-list/1
"""

def delete_all(head,key):
 node=head
 while node:
  nxt=node.next
  if node.data==key:
   if node.prev:node.prev.next=node.next
   else:head=node.next
   if node.next:node.next.prev=node.prev
  node=nxt
 return head
