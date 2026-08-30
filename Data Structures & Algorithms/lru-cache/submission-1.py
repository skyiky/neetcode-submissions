class Node:
    def __init__(self, key=0, value=0):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.back = Node()
        self.front = self.back
        self.hmap = {}

    def update(self, node: Node) -> None:
        if not node.next:
            pass
        else:
            A = node.prev # Remove
            B = node
            C = node.next
            A.next = C  # A <--> B <--> C 
            C.prev = A  # A <--> C

            B.prev = self.front # Insert at front
            B.next = None
            self.front.next = B
            self.front = B # ... <--> B <-- front

    def get(self, key: int) -> int:
        if key in self.hmap:
            self.update(self.hmap[key])
            return self.front.value
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.hmap: # No eviction required
            self.update(self.hmap[key])
            self.front.value = value
        else:
            if self.capacity > 0: # Insert at front
                self.capacity -= 1
                node = Node(key, value)

                node.prev = self.front
                self.front.next = node

                self.front = node # Update front
                self.hmap[key] = node # Create hashmap entry
            else: # Evict and insert
                node = self.back.next # Node to evict
                oldkey = node.key 

                node.key = key # Overwrite
                node.value = value

                self.update(node)
                self.hmap[key] = node # add new entry
                del self.hmap[oldkey] # delete old entry














