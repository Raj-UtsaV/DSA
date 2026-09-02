"""Canonical solution metadata.

Problem Number: 54
Problem Title: Spiral Matrix
Platform: LeetCode
Difficulty: Medium
Official Platform Topics: Array, Matrix, Simulation
Study Tags: Boundary Traversal
Canonical URL: https://leetcode.com/problems/spiral-matrix/
"""

class Solution:
 def spiralOrder(self,matrix):
  out=[]
  while matrix:
   out+=matrix.pop(0)
   if matrix and matrix[0]:
    for row in matrix:out.append(row.pop())
   if matrix:out+=matrix.pop()[::-1]
   if matrix and matrix[0]:
    for row in matrix[::-1]:out.append(row.pop(0))
  return out
