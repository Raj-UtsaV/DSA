"""Canonical solution metadata.

Problem Number: Not applicable
Problem Title: Find Nth Root of M
Platform: Code360
Difficulty: Not reliably specified
Official Platform Topics: Not specified
Study Tags: Binary Search
Canonical URL: https://www.naukri.com/code360/problems/nth-root-of-m_1062679
"""

def nth_root(n,m):
 left,right=1,m
 while left<=right:
  mid=(left+right)//2;value=mid**n
  if value==m:return mid
  if value<m:left=mid+1
  else:right=mid-1
 return -1
