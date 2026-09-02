"""Canonical solution metadata.

Problem Number: Not applicable
Problem Title: Rotation Count in Rotated Sorted Array
Platform: Other
Difficulty: Not reliably specified
Official Platform Topics: Not specified
Study Tags: Binary Search, Rotation Pivot
Canonical URL: Unresolved
"""

def rotation_count(values):
 left,right=0,len(values)-1
 while left<right:
  mid=(left+right)//2
  if values[mid]>values[right]:left=mid+1
  else:right=mid
 return left
