"""Canonical solution metadata.

Problem Number: 992
Problem Title: Subarrays with K Different Integers
Platform: LeetCode
Difficulty: Hard
Official Platform Topics: Array, Hash Table, Sliding Window, Counting
Study Tags: Exactly K via At Most K
Canonical URL: https://leetcode.com/problems/subarrays-with-k-different-integers/
"""

from collections import defaultdict
class Solution:
 def subarraysWithKDistinct(self,nums,k):
  def at_most(limit):
   count=defaultdict(int);left=ans=0
   for right,x in enumerate(nums):
    if count[x]==0:limit-=1
    count[x]+=1
    while limit<0:count[nums[left]]-=1;limit+=count[nums[left]]==0;left+=1
    ans+=right-left+1
   return ans
  return at_most(k)-at_most(k-1)
