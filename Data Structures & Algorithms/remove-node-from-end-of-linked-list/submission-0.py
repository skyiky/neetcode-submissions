# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        tail = head
        for _ in range(n-1):
            tail = tail.next
        
        prev, curr = None, head
        while tail.next:
            tail = tail.next
            prev = curr
            curr = curr.next
        
        if prev:
            prev.next = curr.next
        else:
            head = curr.next
        curr.next = None

        return head
        



        


            