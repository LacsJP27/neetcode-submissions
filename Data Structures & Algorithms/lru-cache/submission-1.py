class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}
        self.front = self.back = Node(0, 0)
        self.front.prev, self.back.next = self.back, self.front
    
    def insert(self, node):
        prev, nxt = self.front.prev, self.front
        prev.next = nxt.prev = node
        node.next, node.prev = nxt, prev
    
    def remove(self, node):
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev

    def get(self, key: int) -> int:
        # update lru
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])

            return self.cache[key].value

        return -1

    def put(self, key: int, value: int) -> None:
        #update lru
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])
        if len(self.cache) > self.cap:
            lru = self.back.next
            self.remove(self.back.next)
            del self.cache[lru.key]


        
