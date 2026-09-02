"""Canonical solution metadata.

Problem Number: 42
Problem Title: Trapping Rain Water
Platform: LeetCode
Difficulty: Hard
Official Platform Topics: Array, Two Pointers, Dynamic Programming, Stack, Monotonic Stack
Study Tags: Two Pointers
Canonical URL: https://leetcode.com/problems/trapping-rain-water/
"""

class Solution:
 def trap(self,height):
  left,right=0,len(height)-1;lm=rm=ans=0
  while left<=right:
   if lm<=rm:lm=max(lm,height[left]);ans+=lm-height[left];left+=1
   else:rm=max(rm,height[right]);ans+=rm-height[right];right-=1
  return ans
