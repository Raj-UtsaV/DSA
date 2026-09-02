"""Canonical solution metadata.

Problem Number: Not applicable
Problem Title: Second Largest Element
Platform: GeeksforGeeks
Difficulty: Easy
Official Platform Topics: Not specified
Study Tags: Array
Canonical URL: https://www.geeksforgeeks.org/problems/second-largest3735/1
"""

def second_largest(values):
 first=second=float("-inf")
 for x in values:
  if x>first:second,first=first,x
  elif first>x>second:second=x
 return -1 if second==float("-inf") else second
