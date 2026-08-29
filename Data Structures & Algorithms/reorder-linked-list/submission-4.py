# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # FIND → CUT → REVERSE → WEAVE
    # 1. Find the middle.
    # 2. Cut with slow.next = None.
    # 3. Reverse only the second half.
    # 4. Weave one node from each half.
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        prev = None
        curr = slow.next # head of "second half" of list
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
            p1.next = p2 # link
            p2.next = p1_next # link
            p1 = p1_next # move up
            p2 = p2_next # move up

