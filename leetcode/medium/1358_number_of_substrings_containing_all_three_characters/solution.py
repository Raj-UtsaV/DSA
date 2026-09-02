"""Canonical solution metadata.

Problem Number: 1358
Problem Title: Number of Substrings Containing All Three Characters
Platform: LeetCode
Difficulty: Medium
Official Platform Topics: Hash Table, String, Sliding Window
Study Tags: Last Seen Indices
Canonical URL: https://leetcode.com/problems/number-of-substrings-containing-all-three-characters/
"""

class Solution:
 def numberOfSubstrings(self,s):
  last=[-1]*3;ans=0
  for i,ch in enumerate(s):last[ord(ch)-97]=i;ans+=1+min(last)
  return ans
