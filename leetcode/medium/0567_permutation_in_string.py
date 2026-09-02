"""Canonical solution metadata.

Problem Number: 567
Problem Title: Permutation in String
Platform: LeetCode
Difficulty: Medium
Official Platform Topics: Hash Table, Two Pointers, String, Sliding Window
Study Tags: Fixed Frequency Window
Canonical URL: https://leetcode.com/problems/permutation-in-string/
"""

from collections import Counter
class Solution:
 def checkInclusion(self,s1,s2):
  need=Counter(s1);window=Counter(s2[:len(s1)])
  if need==window:return True
  for i in range(len(s1),len(s2)):
   window[s2[i]]+=1;old=s2[i-len(s1)];window[old]-=1
   if not window[old]:del window[old]
   if need==window:return True
  return False
