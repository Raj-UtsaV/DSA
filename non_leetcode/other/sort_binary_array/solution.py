"""Canonical solution metadata.

Problem Number: Not applicable
Problem Title: Sort Binary Array
Platform: Other
Difficulty: Not reliably specified
Official Platform Topics: Not specified
Study Tags: Two Pointers
Canonical URL: Unresolved
"""

def sort_binary(values):
 left,right=0,len(values)-1
 while left<right:
  while left<right and values[left]==0:left+=1
  while left<right and values[right]==1:right-=1
  if left<right:values[left],values[right]=values[right],values[left]
 return values
