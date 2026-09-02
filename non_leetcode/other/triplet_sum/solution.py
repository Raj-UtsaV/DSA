"""Canonical solution metadata.

Problem Number: Not applicable
Problem Title: Triplet Sum
Platform: Other
Difficulty: Not reliably specified
Official Platform Topics: Not specified
Study Tags: Sorting, Two Pointers
Canonical URL: Unresolved
"""

def triplet_sum(values,target):
 values=sorted(values);out=[]
 for i in range(len(values)-2):
  if i and values[i]==values[i-1]:continue
  left,right=i+1,len(values)-1
  while left<right:
   total=values[i]+values[left]+values[right]
   if total==target:out.append((values[i],values[left],values[right]));left+=1;right-=1
   elif total<target:left+=1
   else:right-=1
 return out
