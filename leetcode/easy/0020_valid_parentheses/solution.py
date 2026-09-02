"""Canonical solution metadata.

Problem Number: 20
Problem Title: Valid Parentheses
Platform: LeetCode
Difficulty: Easy
Official Platform Topics: String, Stack, Bracket Sequences
Study Tags: Delimiter Matching
Canonical URL: https://leetcode.com/problems/valid-parentheses/
"""

class Solution:
 def isValid(self,s):
  stack=[];pairs={')':'(',']':'[','}':'{'}
  for ch in s:
   if ch in pairs:
    if not stack or stack.pop()!=pairs[ch]:return False
   else:stack.append(ch)
  return not stack
