"""Canonical solution metadata.

Problem Number: 435
Problem Title: Non-overlapping Intervals
Platform: LeetCode
Difficulty: Medium
Official Platform Topics: Array, Dynamic Programming, Greedy, Sorting
Study Tags: Activity Selection
Canonical URL: https://leetcode.com/problems/non-overlapping-intervals/
"""

class Solution:
 def eraseOverlapIntervals(self,intervals):
  end=float("-inf");keep=0
  for start,finish in sorted(intervals,key=lambda x:x[1]):
   if start>=end:keep+=1;end=finish
  return len(intervals)-keep
