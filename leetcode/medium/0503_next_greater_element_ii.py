"""Canonical solution metadata.

Problem Number: 503
Problem Title: Next Greater Element II
Platform: LeetCode
Difficulty: Medium
Official Platform Topics: Array, Stack, Monotonic Stack
Study Tags: Circular Monotonic Stack
Canonical URL: https://leetcode.com/problems/next-greater-element-ii/
"""

class Solution:
 def nextGreaterElements(self,nums):
  n=len(nums);out=[-1]*n;stack=[]
  for i in range(2*n):
   while stack and nums[stack[-1]]<nums[i%n]:out[stack.pop()]=nums[i%n]
   if i<n:stack.append(i)
  return out
