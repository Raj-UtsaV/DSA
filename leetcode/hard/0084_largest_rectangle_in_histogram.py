"""Canonical solution metadata.

Problem Number: 84
Problem Title: Largest Rectangle in Histogram
Platform: LeetCode
Difficulty: Hard
Official Platform Topics: Array, Stack, Monotonic Stack, Range Minimum/Maximum Query
Study Tags: Previous Smaller Element
Canonical URL: https://leetcode.com/problems/largest-rectangle-in-histogram/
"""

class Solution:
 def largestRectangleArea(self,heights):
  stack=[];best=0
  for i,h in enumerate(heights+[0]):
   start=i
   while stack and stack[-1][1]>h:j,height=stack.pop();best=max(best,height*(i-j));start=j
   stack.append((start,h))
  return best
