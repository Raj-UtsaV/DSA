"""Canonical solution metadata.

Problem Number: 1248
Problem Title: Count Number of Nice Subarrays
Platform: LeetCode
Difficulty: Medium
Official Platform Topics: Array, Hash Table, Math, Sliding Window, Prefix Sum
Study Tags: Prefix Frequency
Canonical URL: https://leetcode.com/problems/count-number-of-nice-subarrays/
"""

from collections import defaultdict
class Solution:
 def numberOfSubarrays(self,nums,k):
  count=defaultdict(int,{0:1});odd=ans=0
  for x in nums:odd+=x&1;ans+=count[odd-k];count[odd]+=1
  return ans
