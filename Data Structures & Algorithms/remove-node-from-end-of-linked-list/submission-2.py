# When to use dummy: 
#   "Could the returned head be different from the original head?"
#   Use a dummy node when the first real node might need special treatment.
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        slow = dummy
        fast = head
        for _ in range(n): # Create an n-node gap
            fast = fast.next
        while fast: # slow stops immediately before the node to remove.
            slow = slow.next
            fast = fast.next
        # Visualization Aid:
        # When SETTING 'next' --> An arrow dangling off the current node
        # When GETTING 'next' --> The actual node being referenced (target)
        slow.next = slow.next.next
        return dummy.next # avoid special handling when removing head.
                    