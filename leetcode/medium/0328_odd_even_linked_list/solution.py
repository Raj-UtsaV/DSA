"""Canonical solution metadata.

Problem Number: 328
Problem Title: Odd Even Linked List
Platform: LeetCode
Difficulty: Medium
Official Platform Topics: Linked List
Study Tags: Pointer Partitioning
Canonical URL: https://leetcode.com/problems/odd-even-linked-list/
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val, self.next = val, next

class Solution:
    def oddEvenList(self, head):
        if not head: return None
        odd=head; even=head.next; even_head=even
        while even and even.next: odd.next=even.next; odd=odd.next; even.next=odd.next; even=even.next
        odd.next=even_head; return head
