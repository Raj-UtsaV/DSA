"""Canonical solution metadata.

Problem Number: 930
Problem Title: Binary Subarrays With Sum
Platform: LeetCode
Difficulty: Medium
Official Platform Topics: Array, Hash Table, Sliding Window, Prefix Sum
Study Tags: Prefix Frequency
Canonical URL: https://leetcode.com/problems/binary-subarrays-with-sum/
"""

from collections import defaultdict
class Solution:
 def numSubarraysWithSum(self,nums,goal):
  count=defaultdict(int,{0:1});total=ans=0
  for x in nums:total+=x;ans+=count[total-goal];count[total]+=1
  return ans
