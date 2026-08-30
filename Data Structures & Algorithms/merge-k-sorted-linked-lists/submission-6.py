# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Divide and conquer is not automatically faster. It works well when:
# - Subproblems can be solved independently.
# - Each division makes them substantially smaller.
# - Combining their answers is efficient.
# - Work from earlier levels does not need to be repeated.
class Solution:    
    # Each level processes all N nodes, and there are about log k levels:
    # N work per level × log(k) levels
    # = O(N log k)
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        
        while len(lists) > 1:
            merged = []
            for i in range(0, len(lists), 2):
                left = lists[i]
                right = lists[i+1] if i+1 < len(lists) else None
                merged.append(self.mergeTwoLists(left, right))
            lists = merged
        
        return lists[0]
            

    def mergeTwoLists(self, left: Optional[ListNode], right: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        tail = dummy
        while left and right:
            if left.val <= right.val:
                tail.next = left
                left = left.next
            else:
                tail.next = right
                right = right.next
            tail = tail.next

        tail.next = left if left else right
        return dummy.next