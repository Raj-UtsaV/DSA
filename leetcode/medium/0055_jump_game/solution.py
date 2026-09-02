"""Canonical solution metadata.

Problem Number: 55
Problem Title: Jump Game
Platform: LeetCode
Difficulty: Medium
Official Platform Topics: Array, Dynamic Programming, Greedy
Study Tags: Farthest Reachable Index
Canonical URL: https://leetcode.com/problems/jump-game/
"""

class Solution:
 def canJump(self,nums):
  far=0
  for i,x in enumerate(nums):
   if i>far:return False
   far=max(far,i+x)
  return True
