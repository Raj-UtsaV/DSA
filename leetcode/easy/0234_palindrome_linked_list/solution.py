"""Canonical solution metadata.

Problem Number: 234
Problem Title: Palindrome Linked List
Platform: LeetCode
Difficulty: Easy
Official Platform Topics: Linked List, Two Pointers, Stack, Recursion
Study Tags: Fast/Slow Pointers, Reverse Second Half
Canonical URL: https://leetcode.com/problems/palindrome-linked-list/
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val, self.next = val, next

class Solution:
    def isPalindrome(self, head):
        slow=fast=head
        while fast and fast.next: slow=slow.next; fast=fast.next.next
        previous=None
        while slow: slow.next,previous,slow=previous,slow,slow.next
        while previous:
            if head.val!=previous.val: return False
            head=head.next; previous=previous.next
        return True
