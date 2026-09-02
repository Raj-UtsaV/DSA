"""Canonical solution metadata.

Problem Number: 225
Problem Title: Implement Stack using Queues
Platform: LeetCode
Difficulty: Easy
Official Platform Topics: Stack, Design, Queue
Study Tags: Queue Rotation
Canonical URL: https://leetcode.com/problems/implement-stack-using-queues/
"""

from collections import deque
class MyStack:
 def __init__(self):self.q=deque()
 def push(self,x):
  self.q.append(x)
  for _ in range(len(self.q)-1):self.q.append(self.q.popleft())
 def pop(self):return self.q.popleft()
 def top(self):return self.q[0]
 def empty(self):return not self.q
