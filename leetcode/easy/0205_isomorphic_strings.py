"""Canonical solution metadata.

Problem Number: 205
Problem Title: Isomorphic Strings
Platform: LeetCode
Difficulty: Easy
Official Platform Topics: Hash Table, String
Study Tags: Bidirectional Mapping
Canonical URL: https://leetcode.com/problems/isomorphic-strings/
"""

class Solution:
 def isIsomorphic(self,s,t):
  if len(s)!=len(t):return False
  forward={};backward={}
  for a,b in zip(s,t):
   if forward.get(a,b)!=b or backward.get(b,a)!=a:return False
   forward[a]=b;backward[b]=a
  return True
