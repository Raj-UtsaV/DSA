"""Canonical solution metadata.

Problem Number: 142
Problem Title: Linked List Cycle II
Platform: LeetCode
Difficulty: Medium
Official Platform Topics: Hash Table, Linked List, Two Pointers, Floyd's Cycle Finding Algorithm
Study Tags: Floyd's Cycle Detection, Fast/Slow Pointers
Canonical URL: https://leetcode.com/problems/linked-list-cycle-ii/
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val, self.next = val, next

class Solution:
    def detectCycle(self, head):
        slow=fast=head
        while fast and fast.next:
            slow=slow.next; fast=fast.next.next
            if slow is fast:
                slow=head
                while slow is not fast: slow=slow.next; fast=fast.next
                return slow
        return None
