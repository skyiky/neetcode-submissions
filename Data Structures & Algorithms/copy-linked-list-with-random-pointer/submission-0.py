"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        hmap = {None: None} # explicit mapping for 'None' required
        curr = head
        while curr:
            hmap[curr] = Node(curr.val)
            curr = curr.next
        
        curr = head
        while curr:
            copy = hmap[curr]
            copy.next = hmap[curr.next]
            copy.random = hmap[curr.random]
            curr = curr.next
        
        return hmap[head]
    