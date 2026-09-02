"""Canonical solution metadata.

Problem Number: Not applicable
Problem Title: Maps-STL
Platform: HackerRank
Difficulty: Easy
Official Platform Topics: Not specified
Study Tags: Map, Frequency Table
Canonical URL: https://www.hackerrank.com/challenges/cpp-maps/problem
"""

def process_queries(queries):
 marks={};out=[]
 for query in queries:
  if query[0]==1:marks[query[1]]=marks.get(query[1],0)+query[2]
  elif query[0]==2:marks.pop(query[1],None)
  else:out.append(marks.get(query[1],0))
 return out
