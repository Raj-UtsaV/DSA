"""Canonical solution metadata.

Problem Number: 160
Problem Title: Intersection of Two Linked Lists
Platform: LeetCode
Difficulty: Easy
Official Platform Topics: Hash Table, Linked List, Two Pointers
Study Tags: Pointer Switching
Canonical URL: https://leetcode.com/problems/intersection-of-two-linked-lists/
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val, self.next = val, next

class Solution:
    def getIntersectionNode(self, headA, headB):
        a,b=headA,headB
        while a is not b: a=a.next if a else headB; b=b.next if b else headA
        return a
