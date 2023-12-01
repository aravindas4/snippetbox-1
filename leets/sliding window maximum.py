class Queue:
    def __init__(self, cap=(10**9+7)):
        self.N = cap
        self.size = 0
        self.f = -1
        self.r = -1
        self.arr = []

    def enqueue(self, x):
        if self.size == self.N:
            return False

        self.r = (self.r + 1) % self.N
        self.size += 1
        self.arr.append(x)
        return True

    def is_empty(self):
        return self.size == 0

    def deque(self):
        if self.is_empty():
            return False

        self.f = (self.f + 1) % self.N
        self.size -= 1
        return self.arr[self.f]

    def front(self):
        if self.is_empty():
            return None

        return self.arr[(self.f + 1) % self.N]

    def remove(self):
        if self.is_empty():
            return None

        self.r = (self.r - 1) % self.N
        self.size -= 1
        return self.arr.pop()

    def rear(self):
        if self.is_empty():
            return None

        return self.arr[self.r]


class Solution:
	# @param A : tuple of integers
	# @param B : integer
	# @return a list of integers
    def slidingMaximum(self, A, B):
        q = Queue()
        ans = []
        N = len(A)

        for i in range(0, B):
            # print("e=", A[i])
            while q.rear() is not None and A[q.rear()] <= A[i]:
                q.remove()

            q.enqueue(i)

        while not (i-B+1 <= q.front() <= i):
            q.deque()

        # print(A[q.front()], q.arr)
        ans.append(A[q.front()])
        
        for i in range(B, N):
            while q.rear() is not None and A[q.rear()] <= A[i]:
                q.remove()

            q.enqueue(i)

            while not (i-B+1 <= q.front() <= i):
                q.deque()

            ans.append(A[q.front()])
        
        return ans

s = Solution()
A = [648,614,490,138,657,544,745,582,738,229,775,665,876,448,4,81,807,578,712,951,867,328,308,440,542,178,637,446,882,760,354,523,935,277,158,698,536,165,892,327,574,516,36,705,900,482,558,937,207,368]
print(s.slidingMaximum(A, 9))