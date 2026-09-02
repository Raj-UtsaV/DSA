"""Canonical solution metadata.

Problem Number: 340
Problem Title: Longest Substring with At Most K Distinct Characters
Platform: LeetCode
Difficulty: Medium
Official Platform Topics: Hash Table, String, Sliding Window
Study Tags: Frequency Window
Canonical URL: https://leetcode.com/problems/longest-substring-with-at-most-k-distinct-characters/
"""

from collections import defaultdict
class Solution:
 def lengthOfLongestSubstringKDistinct(self,s,k):
  count=defaultdict(int);left=ans=0
  for right,ch in enumerate(s):
   count[ch]+=1
   while len(count)>k:
    old=s[left];count[old]-=1;left+=1
    if not count[old]:del count[old]
   ans=max(ans,right-left+1)
  return ans
