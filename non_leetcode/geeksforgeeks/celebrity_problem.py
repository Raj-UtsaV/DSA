"""Canonical solution metadata.

Problem Number: Not applicable
Problem Title: Celebrity Problem
Platform: GeeksforGeeks
Difficulty: Not reliably specified
Official Platform Topics: Not specified
Study Tags: Elimination
Canonical URL: https://www.geeksforgeeks.org/problems/the-celebrity-problem/1
"""

def celebrity(matrix):
 candidate=0
 for person in range(1,len(matrix)):
  if matrix[candidate][person]:candidate=person
 return candidate if all(i==candidate or matrix[i][candidate] and not matrix[candidate][i] for i in range(len(matrix))) else -1
