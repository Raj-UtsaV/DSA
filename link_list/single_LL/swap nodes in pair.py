
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        temp = head
        head = head.next
        prev = None

        while temp and temp.next:
                Next_p = temp.next.next
                second = temp.next
                second.next = temp
                temp.next = Next_p
                
                if prev:
                    prev.next = second
                
                prev = temp
                temp = Next_p

        return head
            