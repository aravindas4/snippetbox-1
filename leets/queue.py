class Queue:
    def __init__(self, cap=(10**9)+7):
        self.cap = cap
        self.arr = []
        self.size = 0
        self.f = -1
        self.rear = -1

    def enqueue(self, x):
        if self.size == self.cap:
            return False

        self.rear = (self.rear + 1) % self.cap
        self.arr.append(x)
        self.size += 1
        return True

    def dequeue(self):
        if self.size == 0:
            return None

        self.f = (self.f + 1) % self.cap
        self.size -= 1
        return self.arr[self.f]

    def front(self):
        if self.size == 0:
            return None

        return self.arr[(self.f + 1) % self.cap]

q = Queue()

q.enqueue(11)
q.enqueue(22)
print(q.front())
q.enqueue(33)
print(q.dequeue())
print(q.front())
print(q.f, q.rear, q.arr)
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
print(q.f, q.rear, q.arr)