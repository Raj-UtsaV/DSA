"""Canonical solution metadata.

Problem Number: 146
Problem Title: LRU Cache
Platform: LeetCode
Difficulty: Medium
Official Platform Topics: Hash Table, Linked List, Design, Doubly-Linked List
Study Tags: Eviction Policy
Canonical URL: https://leetcode.com/problems/lru-cache/
"""

from collections import OrderedDict
class LRUCache:
 def __init__(self,capacity):self.capacity=capacity;self.data=OrderedDict()
 def get(self,key):
  if key not in self.data:return -1
  self.data.move_to_end(key);return self.data[key]
 def put(self,key,value):
  self.data[key]=value;self.data.move_to_end(key)
  if len(self.data)>self.capacity:self.data.popitem(last=False)
