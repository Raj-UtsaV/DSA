"""Canonical solution metadata.

Problem Number: 727
Problem Title: Minimum Window Subsequence
Platform: LeetCode
Difficulty: Hard
Official Platform Topics: String, Dynamic Programming, Sliding Window
Study Tags: Forward and Backward Scan
Canonical URL: https://leetcode.com/problems/minimum-window-subsequence/
"""

class Solution:
 def minWindow(self,s1,s2):
  best="";i=0
  while i<len(s1):
   j=0
   while i<len(s1) and j<len(s2):j+=s1[i]==s2[j];i+=1
   if j<len(s2):break
   end=i;j-=1;i-=1
   while j>=0:j-=s1[i]==s2[j];i-=1
   i+=1;candidate=s1[i:end]
   if not best or len(candidate)<len(best):best=candidate
   i+=1
  return best
