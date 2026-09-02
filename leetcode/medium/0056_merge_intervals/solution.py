"""Canonical solution metadata.

Problem Number: 56
Problem Title: Merge Intervals
Platform: LeetCode
Difficulty: Medium
Official Platform Topics: Array, Sorting, Quicksort
Study Tags: Interval Merging
Canonical URL: https://leetcode.com/problems/merge-intervals/
"""

class Solution:
 def merge(self,intervals):
  out=[]
  for start,end in sorted(intervals):
   if out and start<=out[-1][1]:out[-1][1]=max(out[-1][1],end)
   else:out.append([start,end])
  return out
