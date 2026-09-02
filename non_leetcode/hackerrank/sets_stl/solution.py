"""Canonical solution metadata.

Problem Number: Not applicable
Problem Title: Sets-STL
Platform: HackerRank
Difficulty: Easy
Official Platform Topics: Not specified
Study Tags: Set
Canonical URL: https://www.hackerrank.com/challenges/cpp-sets/problem
"""

def process_queries(queries):
 values=set();out=[]
 for operation,value in queries:
  if operation==1:values.add(value)
  elif operation==2:values.discard(value)
  else:out.append("Yes" if value in values else "No")
 return out
