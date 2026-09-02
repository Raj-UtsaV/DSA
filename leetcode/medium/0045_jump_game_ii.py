"""Canonical solution metadata.

Problem Number: 45
Problem Title: Jump Game II
Platform: LeetCode
Difficulty: Medium
Official Platform Topics: Array, Dynamic Programming, Greedy
Study Tags: Greedy Range Expansion
Canonical URL: https://leetcode.com/problems/jump-game-ii/
"""

class Solution:
 def jump(self,nums):
  jumps=end=far=0
  for i in range(len(nums)-1):
   far=max(far,i+nums[i])
   if i==end:jumps+=1;end=far
  return jumps
