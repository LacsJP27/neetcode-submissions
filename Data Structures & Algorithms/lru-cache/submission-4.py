class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        # initialize of size capacity
        # key used if a get or a put operation is called on it
        self.capacity = capacity
        self.cache = {}
        self.new =  Node(0,0)
        self.old = Node(0,0)
        self.old.next, self.new.prev = self.new, self.old

    def insert(self, node):
        prev, nxt = self.new.prev, self.new
        prev.next, node.prev = node, prev
        node.next, self.new.prev = nxt, node
          
    def remove(self, node):
        nxt, prev = node.next, node.prev
        prev.next = nxt
        nxt.prev = prev

    def get(self, key: int) -> int:
        # return the value at that key and update recently used
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].value

        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])

        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        if len(self.cache) > self.capacity:
            lru = self.old.next
            self.remove(lru)
            del self.cache[lru.key]





      
