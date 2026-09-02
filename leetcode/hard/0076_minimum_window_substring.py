"""Canonical solution metadata.

Problem Number: 76
Problem Title: Minimum Window Substring
Platform: LeetCode
Difficulty: Hard
Official Platform Topics: Hash Table, String, Sliding Window
Study Tags: Frequency Deficit
Canonical URL: https://leetcode.com/problems/minimum-window-substring/
"""

from collections import Counter
class Solution:
 def minWindow(self,s,t):
  need=Counter(t);missing=len(t);left=start=end=0
  for right,ch in enumerate(s,1):
   if need[ch]>0:missing-=1
   need[ch]-=1
   if missing==0:
    while left<right and need[s[left]]<0:need[s[left]]+=1;left+=1
    if end==0 or right-left<end-start:start,end=left,right
    need[s[left]]+=1;missing+=1;left+=1
  return s[start:end]
