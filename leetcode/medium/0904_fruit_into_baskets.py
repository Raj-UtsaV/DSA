"""Canonical solution metadata.

Problem Number: 904
Problem Title: Fruit Into Baskets
Platform: LeetCode
Difficulty: Medium
Official Platform Topics: Array, Hash Table, Sliding Window
Study Tags: At Most Two Distinct
Canonical URL: https://leetcode.com/problems/fruit-into-baskets/
"""

from collections import defaultdict
class Solution:
 def totalFruit(self,fruits):
  count=defaultdict(int);left=ans=0
  for right,x in enumerate(fruits):
   count[x]+=1
   while len(count)>2:
    y=fruits[left];count[y]-=1;left+=1
    if not count[y]:del count[y]
   ans=max(ans,right-left+1)
  return ans
