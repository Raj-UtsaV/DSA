"""Canonical solution metadata.

Problem Number: Not applicable
Problem Title: Allocate Minimum Pages
Platform: GeeksforGeeks
Difficulty: Not reliably specified
Official Platform Topics: Not specified
Study Tags: Binary Search on Answer, Greedy Feasibility
Canonical URL: https://www.geeksforgeeks.org/problems/allocate-minimum-number-of-pages0937/1
"""

def find_pages(pages,students):
 if students>len(pages):return -1
 def needed(limit):
  groups=1;total=0
  for page in pages:
   if total+page>limit:groups+=1;total=0
   total+=page
  return groups
 left,right=max(pages),sum(pages)
 while left<right:
  mid=(left+right)//2
  if needed(mid)<=students:right=mid
  else:left=mid+1
 return left
