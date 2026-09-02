"""Canonical solution metadata.

Problem Number: 2095
Problem Title: Delete the Middle Node of a Linked List
Platform: LeetCode
Difficulty: Medium
Official Platform Topics: Linked List, Two Pointers
Study Tags: Fast/Slow Pointers
Canonical URL: https://leetcode.com/problems/delete-the-middle-node-of-a-linked-list/
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val, self.next = val, next

class Solution:
    def deleteMiddle(self, head):
        if not head.next: return None
        slow=head; fast=head.next.next
        while fast and fast.next: slow=slow.next; fast=fast.next.next
        slow.next=slow.next.next; return head
