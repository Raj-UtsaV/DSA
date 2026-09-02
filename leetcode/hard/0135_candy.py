"""Canonical solution metadata.

Problem Number: 135
Problem Title: Candy
Platform: LeetCode
Difficulty: Hard
Official Platform Topics: Array, Greedy
Study Tags: Two Directional Passes
Canonical URL: https://leetcode.com/problems/candy/
"""

class Solution:
 def candy(self,ratings):
  n=len(ratings);c=[1]*n
  for i in range(1,n):
   if ratings[i]>ratings[i-1]:c[i]=c[i-1]+1
  for i in range(n-2,-1,-1):
   if ratings[i]>ratings[i+1]:c[i]=max(c[i],c[i+1]+1)
  return sum(c)
