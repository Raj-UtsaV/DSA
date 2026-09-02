"""Canonical solution metadata.

Problem Number: 402
Problem Title: Remove K Digits
Platform: LeetCode
Difficulty: Medium
Official Platform Topics: String, Stack, Greedy, Monotonic Stack
Study Tags: Monotonic Stack
Canonical URL: https://leetcode.com/problems/remove-k-digits/
"""

class Solution:
 def removeKdigits(self,num,k):
  stack=[]
  for ch in num:
   while k and stack and stack[-1]>ch:stack.pop();k-=1
   stack.append(ch)
  if k:stack=stack[:-k]
  return ''.join(stack).lstrip('0') or '0'
