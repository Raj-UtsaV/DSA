"""Canonical solution metadata.

Problem Number: 2
Problem Title: Add Two Numbers
Platform: LeetCode
Difficulty: Medium
Official Platform Topics: Linked List, Math, Recursion
Study Tags: Carry Propagation
Canonical URL: https://leetcode.com/problems/add-two-numbers/
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val, self.next = val, next

class Solution:
    def addTwoNumbers(self, l1, l2):
        dummy=tail=ListNode(); carry=0
        while l1 or l2 or carry:
            total=carry+(l1.val if l1 else 0)+(l2.val if l2 else 0); carry,value=divmod(total,10)
            tail.next=ListNode(value); tail=tail.next
            l1=l1.next if l1 else None; l2=l2.next if l2 else None
        return dummy.next
