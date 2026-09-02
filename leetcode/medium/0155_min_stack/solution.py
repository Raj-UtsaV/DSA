"""Canonical solution metadata.

Problem Number: 155
Problem Title: Min Stack
Platform: LeetCode
Difficulty: Medium
Official Platform Topics: Stack, Design
Study Tags: Auxiliary Minimum
Canonical URL: https://leetcode.com/problems/min-stack/
"""

class MinStack:
 def __init__(self):self.stack=[]
 def push(self,val):self.stack.append((val,min(val,self.stack[-1][1]) if self.stack else val))
 def pop(self):self.stack.pop()
 def top(self):return self.stack[-1][0]
 def getMin(self):return self.stack[-1][1]
