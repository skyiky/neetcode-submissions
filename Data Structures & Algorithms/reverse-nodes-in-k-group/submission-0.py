    # Definition for singly-linked list.
    # class ListNode:
    #     def __init__(self, val=0, next=None):
    #         self.val = val
    #         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(next=head)

        last_group_tail = dummy
        old_head = head
        old_tail = head
        count = k

        while old_tail:
            old_tail = old_tail.next
            count -= 1

            if old_tail is None and count > 0:
                return dummy.next

            if count == 0:
                curr = old_head
                prev = old_tail

                for _ in range(k):
                    next_node = curr.next
                    curr.next = prev
                    prev = curr
                    curr = next_node

                last_group_tail.next = prev
                last_group_tail = old_head

                old_head = curr
                old_tail = curr
                count = k

        return dummy.next