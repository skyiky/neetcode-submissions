# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)

        group_prev = dummy 

        while True:
            # Locate
            kth = self.getKth(group_prev, k)
            if kth is None:
                break
            group_next = kth.next

            # Transform
            prev = group_next 
            curr = group_prev.next
            while curr != group_next:
                _next = curr.next
                curr.next = prev
                prev = curr
                curr = _next

            # Reconnect
            _next_group_prev = group_prev.next
            group_prev.next = kth
            group_prev = _next_group_prev
        
        return dummy.next
        
    def getKth(self, node: Optional[ListNode], k) -> Optional[ListNode]:
        while node and k > 0:
            node = node.next
            k -= 1
        return node
        