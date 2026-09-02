"""Canonical solution metadata.

Problem Number: 1423
Problem Title: Maximum Points You Can Obtain from Cards
Platform: LeetCode
Difficulty: Medium
Official Platform Topics: Array, Sliding Window, Prefix Sum
Study Tags: Complement Window
Canonical URL: https://leetcode.com/problems/maximum-points-you-can-obtain-from-cards/
"""

class Solution:
 def maxScore(self,cards,k):
  if k==len(cards):return sum(cards)
  window=sum(cards[:len(cards)-k]);minimum=window
  for i in range(len(cards)-k,len(cards)):window+=cards[i]-cards[i-(len(cards)-k)];minimum=min(minimum,window)
  return sum(cards)-minimum
