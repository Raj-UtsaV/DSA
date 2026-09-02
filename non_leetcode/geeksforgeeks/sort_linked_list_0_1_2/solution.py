"""Canonical solution metadata.

Problem Number: Not applicable
Problem Title: Sort a Linked List of 0s, 1s and 2s
Platform: GeeksforGeeks
Difficulty: Not reliably specified
Official Platform Topics: Not specified
Study Tags: Counting, Linked List
Canonical URL: https://www.geeksforgeeks.org/problems/given-a-linked-list-of-0s-1s-and-2s-sort-it/1
"""

def segregate(head):
 count=[0,0,0];node=head
 while node:count[node.data]+=1;node=node.next
 node=head
 for value,total in enumerate(count):
  for _ in range(total):node.data=value;node=node.next
 return head
