"""Canonical solution metadata.

Problem Number: 424
Problem Title: Longest Repeating Character Replacement
Platform: LeetCode
Difficulty: Medium
Official Platform Topics: Hash Table, String, Sliding Window
Study Tags: Maximum Frequency Window
Canonical URL: https://leetcode.com/problems/longest-repeating-character-replacement/
"""

from collections import defaultdict
class Solution:
 def characterReplacement(self,s,k):
  count=defaultdict(int);left=best=maxf=0
  for right,ch in enumerate(s):
   count[ch]+=1;maxf=max(maxf,count[ch])
   if right-left+1-maxf>k:count[s[left]]-=1;left+=1
   best=max(best,right-left+1)
  return best
