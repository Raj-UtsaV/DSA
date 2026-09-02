"""Canonical solution metadata.

Problem Number: 239
Problem Title: Sliding Window Maximum
Platform: LeetCode
Difficulty: Hard
Official Platform Topics: Array, Queue, Sliding Window, Heap (Priority Queue), Monotonic Queue, Range Minimum/Maximum Query
Study Tags: Monotonic Deque
Canonical URL: https://leetcode.com/problems/sliding-window-maximum/
"""

from collections import deque
class Solution:
 def maxSlidingWindow(self,nums,k):
  q=deque();out=[]
  for i,x in enumerate(nums):
   while q and nums[q[-1]]<=x:q.pop()
   q.append(i)
   if q[0]<=i-k:q.popleft()
   if i>=k-1:out.append(nums[q[0]])
  return out
