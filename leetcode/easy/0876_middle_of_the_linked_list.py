"""Canonical solution metadata.

Problem Number: 876
Problem Title: Middle of the Linked List
Platform: LeetCode
Difficulty: Easy
Official Platform Topics: Linked List, Two Pointers
Study Tags: Fast/Slow Pointers
Canonical URL: https://leetcode.com/problems/middle-of-the-linked-list/
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val, self.next = val, next

class Solution:
    def middleNode(self, head):
        slow=fast=head
        while fast and fast.next: slow=slow.next; fast=fast.next.next
        return slow
