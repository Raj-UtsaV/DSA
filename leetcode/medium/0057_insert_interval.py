"""Canonical solution metadata.

Problem Number: 57
Problem Title: Insert Interval
Platform: LeetCode
Difficulty: Medium
Official Platform Topics: Array
Study Tags: Interval Merging
Canonical URL: https://leetcode.com/problems/insert-interval/
"""

class Solution:
 def insert(self,intervals,newInterval):
  out=[];i=0
  while i<len(intervals) and intervals[i][1]<newInterval[0]:out.append(intervals[i]);i+=1
  while i<len(intervals) and intervals[i][0]<=newInterval[1]:newInterval=[min(newInterval[0],intervals[i][0]),max(newInterval[1],intervals[i][1])];i+=1
  return out+[newInterval]+intervals[i:]
