"""Canonical solution metadata.

Problem Number: Not applicable
Problem Title: Previous Smaller Element
Platform: GeeksforGeeks
Difficulty: Not reliably specified
Official Platform Topics: Not specified
Study Tags: Monotonic Stack
Canonical URL: https://www.geeksforgeeks.org/problems/smallest-number-on-left3403/1
"""

def previous_smaller(values):
 out=[];stack=[]
 for value in values:
  while stack and stack[-1]>=value:stack.pop()
  out.append(stack[-1] if stack else -1);stack.append(value)
 return out
