"""Canonical solution metadata.

Problem Number: 1004
Problem Title: Max Consecutive Ones III
Platform: LeetCode
Difficulty: Medium
Official Platform Topics: Array, Binary Search, Sliding Window, Prefix Sum
Study Tags: Zero Count Window
Canonical URL: https://leetcode.com/problems/max-consecutive-ones-iii/
"""

class Solution:
 def longestOnes(self,nums,k):
  left=0
  for right,x in enumerate(nums):
   k-=x==0
   if k<0:k+=nums[left]==0;left+=1
  return len(nums)-left
