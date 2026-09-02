"""Canonical solution metadata.

Problem Number: 141
Problem Title: Linked List Cycle
Platform: LeetCode
Difficulty: Easy
Official Platform Topics: Hash Table, Linked List, Two Pointers, Floyd's Cycle Finding Algorithm
Study Tags: Floyd's Cycle Detection, Fast/Slow Pointers
Canonical URL: https://leetcode.com/problems/linked-list-cycle/
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val, self.next = val, next

class Solution:
    def hasCycle(self, head):
        slow=fast=head
        while fast and fast.next:
            slow=slow.next; fast=fast.next.next
            if slow is fast: return True
        return False
