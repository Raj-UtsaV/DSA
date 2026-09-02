"""Canonical solution metadata.

Problem Number: Not applicable
Problem Title: Next Larger Element
Platform: GeeksforGeeks
Difficulty: Not reliably specified
Official Platform Topics: Not specified
Study Tags: Monotonic Stack
Canonical URL: https://www.geeksforgeeks.org/problems/next-larger-element-1587115620/1
"""

def next_larger(values):
 out=[-1]*len(values);stack=[]
 for i in range(len(values)-1,-1,-1):
  while stack and stack[-1]<=values[i]:stack.pop()
  if stack:out[i]=stack[-1]
  stack.append(values[i])
 return out
