"""Canonical solution metadata.

Problem Number: 455
Problem Title: Assign Cookies
Platform: LeetCode
Difficulty: Easy
Official Platform Topics: Array, Two Pointers, Greedy, Sorting, Quicksort
Study Tags: Greedy Matching
Canonical URL: https://leetcode.com/problems/assign-cookies/
"""

class Solution:
 def findContentChildren(self,g,s):
  g.sort();s.sort();i=0
  for cookie in s:
   if i<len(g) and cookie>=g[i]:i+=1
  return i
