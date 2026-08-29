# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head
        while curr:
            _next = curr.next # will lose this reference so store it as a variable
            curr.next = prev # actual reversal operation
            prev = curr # move up pointer
            curr = _next # move up point
        return prev