"""Canonical solution metadata.

Problem Number: 19
Problem Title: Remove Nth Node From End of List
Platform: LeetCode
Difficulty: Medium
Official Platform Topics: Linked List, Two Pointers
Study Tags: Fast/Slow Pointers
Canonical URL: https://leetcode.com/problems/remove-nth-node-from-end-of-list/
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val, self.next = val, next

class Solution:
    def removeNthFromEnd(self, head, n):
        dummy=ListNode(0,head); fast=slow=dummy
        for _ in range(n+1): fast=fast.next
        while fast: fast=fast.next; slow=slow.next
        slow.next=slow.next.next; return dummy.next
