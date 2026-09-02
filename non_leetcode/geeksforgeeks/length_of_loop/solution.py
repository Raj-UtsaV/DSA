"""Canonical solution metadata.

Problem Number: Not applicable
Problem Title: Find Length of Loop
Platform: GeeksforGeeks
Difficulty: Not reliably specified
Official Platform Topics: Not specified
Study Tags: Floyd's Cycle Detection
Canonical URL: https://www.geeksforgeeks.org/problems/find-length-of-loop/1
"""

def loop_length(head):
 slow=fast=head
 while fast and fast.next:
  slow=slow.next;fast=fast.next.next
  if slow is fast:
   count=1;fast=fast.next
   while fast is not slow:count+=1;fast=fast.next
   return count
 return 0
