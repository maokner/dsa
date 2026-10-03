class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.items = {}
        self.time = 0
        self.head = Node(-1, -1)
        self.cap = capacity

        #tail is just a pointer to last element
        self.tail = self.head
        self.size = 0

    def makeMostRecent(self, node):
        if self.size == 1:
            return
        if self.head.next == node:
            return 

        if self.tail == node:
            self.tail = node.prev
        
        node.prev.next = node.next
        if node.next:
            node.next.prev = node.prev
        
        node.prev = self.head
        node.next = self.head.next

        self.head.next.prev = node
        self.head.next = node

    def get(self, key: int) -> int:
        if key in self.items:
            ret = self.items[key].value
            self.makeMostRecent(self.items[key])
            return ret

        return -1
        
    def put(self, key: int, value: int) -> None:
        if key in self.items:
            self.items[key].value = value
            self.makeMostRecent(self.items[key])

        else:
            if self.size == self.cap:
                #remove last item
                last = self.tail
                del self.items[last.key]
                self.tail = last.prev
                last.prev.next = None
                self.size -= 1
            newNode = Node(key, value)
            self.items[key] = newNode
            if self.size == 0:
                self.tail = newNode

            newNode.next = self.head.next
            newNode.prev = self.head

            if self.head.next:
                self.head.next.prev = newNode
            self.head.next = newNode
            self.size += 1

        
