# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # Reusable Template
    # dummy = ListNode()
    # tail = dummy
    #
    # while nodes_are_available:
    #   tail.next = chosen_node
    #   tail = tail.next
    #
    # return dummy.next
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode() # permanent pointer
        tail = dummy # construction pointer
    
        while list1 and list2:
            if list1.val <= list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next
        
        tail.next = list1 or list2
        
        return dummy.next