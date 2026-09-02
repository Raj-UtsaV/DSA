"""Canonical solution metadata.

Problem Number: 3
Problem Title: Longest Substring Without Repeating Characters
Platform: LeetCode
Difficulty: Medium
Official Platform Topics: Hash Table, String, Sliding Window
Study Tags: Last Seen Index
Canonical URL: https://leetcode.com/problems/longest-substring-without-repeating-characters/
"""

class Solution:
 def lengthOfLongestSubstring(self,s):
  seen={};left=ans=0
  for right,ch in enumerate(s):left=max(left,seen.get(ch,-1)+1);seen[ch]=right;ans=max(ans,right-left+1)
  return ans
