"""Canonical solution metadata.

Problem Number: Not applicable
Problem Title: Pair Sum
Platform: Other
Difficulty: Not reliably specified
Official Platform Topics: Not specified
Study Tags: Hash Table
Canonical URL: Unresolved
"""

def pair_sum(values,target):
 seen={};out=[]
 for i,x in enumerate(values):
  if target-x in seen:out.append((seen[target-x],i))
  seen[x]=i
 return out
