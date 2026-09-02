"""Canonical solution metadata.

Problem Number: Not applicable
Problem Title: Find Pairs with Given Sum in Doubly Linked List
Platform: GeeksforGeeks
Difficulty: Not reliably specified
Official Platform Topics: Not specified
Study Tags: Two Pointers
Canonical URL: https://www.geeksforgeeks.org/problems/find-pairs-with-given-sum-in-doubly-linked-list/1
"""

def find_pairs(head,target):
 if not head:return []
 left=head;right=head
 while right.next:right=right.next
 out=[]
 while left is not right and right.next is not left:
  total=left.data+right.data
  if total==target:out.append((left.data,right.data));left=left.next;right=right.prev
  elif total<target:left=left.next
  else:right=right.prev
 return out
