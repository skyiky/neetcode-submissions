# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        prev = None
        curr = slow.next
        slow.next = None # disconnect first half from second half
        while curr: # REVERSE LINKED LIST "RFMM" ACRONYM 
            _next = curr.next # remember
            curr.next = prev # flip
            prev = curr # move up
            curr = _next # move up
        
        p1, p2 = head, prev
        while p2:
            p1_next = p1.next # remember
            p2_next = p2.next # remember

            p1.next = p2
            p1 = p1_next
            p2.next = p1
            p2 = p2_next

