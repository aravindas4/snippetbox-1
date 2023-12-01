class ListNode:

    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

class LRUCache:

    # @param capacity, an integer
    def __init__(self, capacity):
        self.head = None
        self.tail = None
        self.hash_map = {}
        self.cap = capacity
        self.size = 0

    # @return an integer
    def get(self, key):
        if key not in self.hash_map:
            return -1

        node = self.hash_map[key]
        self.remove_node(node)
        self.add_to_tail(node)
        return node.val

    def add_to_tail(self, node):
        if self.tail:
            self.tail.next = node
            node.prev = self.tail

        self.tail = node
        if self.head is None:
            self.head = node
        
        if self.size == self.cap and self.head:
            self.hash_map.pop(self.head.key)
            self.head = self.head.next
            self.head.prev = None
        else:
            self.size += 1

    def remove_node(self, node):
        if node == self.head:
            self.head = self.head.next

        if node == self.tail:
            self.tail = self.tail.prev

        if node.next:
            node.next.prev = node.prev

        if node.prev:
            node.prev.next = node.next

        node.next = None
        node.prev = None
        self.size -= 1


    # @param key, an integer
    # @param value, an integer
    # @return nothing
    def set(self, key, value):
        if key in self.hash_map:
            node = self.hash_map[key]
            node.val = value
            self.remove_node(node)
        else:
            node = ListNode(key, value)

        self.hash_map[key] = node
        self.add_to_tail(node)
        self.pprint(self.head)

    def pprint(self, node):
        print(self.hash_map)
        while node:
            # print(node)
            print(node.val, '->', end='')
            node = node.next
        print()

lru = LRUCache(1)
lru.set(2, 1)
lru.set(2, 2)
print(lru.hash_map)
# lru.pprint(lru.head)
print(lru.get(2))
lru.set(1,1)
lru.set(4,1)
print(lru.get(2))



# print(lru.head)
# pprint(lru.head)