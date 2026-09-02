"""Canonical solution metadata.

Problem Number: 1910
Problem Title: Remove All Occurrences of a Substring
Platform: LeetCode
Difficulty: Medium
Official Platform Topics: String, Stack, Simulation
Study Tags: Repeated Erasure
Canonical URL: https://leetcode.com/problems/remove-all-occurrences-of-a-substring/
"""

class Solution:
 def removeOccurrences(self,s,part):
  while part in s:s=s.replace(part,'',1)
  return s
