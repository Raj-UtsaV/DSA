"""Canonical solution metadata.

Problem Number: 860
Problem Title: Lemonade Change
Platform: LeetCode
Difficulty: Easy
Official Platform Topics: Array, Greedy
Study Tags: Change Invariant
Canonical URL: https://leetcode.com/problems/lemonade-change/
"""

class Solution:
 def lemonadeChange(self,bills):
  five=ten=0
  for bill in bills:
   if bill==5:five+=1
   elif bill==10:five-=1;ten+=1
   elif ten:ten-=1;five-=1
   else:five-=3
   if five<0:return False
  return True
