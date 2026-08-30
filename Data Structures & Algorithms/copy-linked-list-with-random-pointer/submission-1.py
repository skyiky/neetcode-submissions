# Important: The copied list does not live inside the hash map (just a directory/reference structure)
# Two solutions: External Hashmap or Interwoven Nodes
class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        hmap = {None: None} # explicit mapping for 'None' required
        curr = head
        while curr: # Pass 1: create a copy of every node 
            hmap[curr] = Node(curr.val)
            curr = curr.next
        
        curr = head
        while curr: # Pass 2: Connect the copied nodes.
            copy = hmap[curr]
            copy.next = hmap[curr.next]
            copy.random = hmap[curr.random] # from the original random, we use the hashmap to find its copy
            curr = curr.next
        
        return hmap[head]
    