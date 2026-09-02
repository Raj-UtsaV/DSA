"""Canonical solution metadata.

Problem Number: 148
Problem Title: Sort List
Platform: LeetCode
Difficulty: Medium
Official Platform Topics: Linked List, Two Pointers, Divide and Conquer, Sorting, Merge Sort
Study Tags: Linked-List Merge Sort
Canonical URL: https://leetcode.com/problems/sort-list/
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val, self.next = val, next

class Solution:
    def sortList(self, head):
        if not head or not head.next: return head
        slow=head; fast=head.next
        while fast and fast.next: slow=slow.next; fast=fast.next.next
        right=slow.next; slow.next=None; left=self.sortList(head); right=self.sortList(right)
        dummy=tail=ListNode()
        while left and right:
            if left.val<=right.val: tail.next,left=left,left.next
            else: tail.next,right=right,right.next
            tail=tail.next
        tail.next=left or right; return dummy.next
