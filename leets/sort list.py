# Definition for singly-linked list.
class ListNode:
	def __init__(self, x):
		self.val = x
		self.next = None

class Solution:
	# @param A : head node of linked list
	# @return the head node in the linked list
    def sortList(self, A):
        return self.mergeL(A)

    def mergeL(self, A):
        if A is None or A.next is None:
            return A

        sp = A
        fp = A

        while fp.next and fp.next.next:
            fp = fp.next.next
            sp = sp.next

        B = sp.next
        # print(B.val, fp.val)
        sp.next = None
        A = self.mergeL(A)
        B = self.mergeL(B)

        
        A = self.merge(A, B)
        # print(A.next)
        return A 
    
    def print(self, A):
        t = A
        s = ''
        while t:
            s += f'{t.val}->'
            t = t.next

        print(s)


    def merge(self, A, B):
        dummy = ListNode(-1)
        tail = dummy
        head = dummy
        self.print(A)
        self.print(B)

        t1 = A 
        t2 = B
        while t1 and t2:
            # print(t1.val, t2.val)
            if t1.val <= t2.val:
                tail.next = t1
                t1 = t1.next
            else:
                tail.next = t2
                t2 = t2.next

            tail = tail.next

        if t1:
            tail.next = t1

        if t2:
            tail.next = t2

        # self.print(head.next)
        return head.next

s = Solution()
# A = [5,66,68,42,73,25,84,63,72,20,77,38,8,99,92,49,74,45,30,51,50,95,56,19,31,26,98,67,
#      100,2,24,6,37,69,11,16,61,23,78,27,64,87,3,85,55,22,33,62]
A = [3,4,2,8]

t = None
start = None
for x in A:
    if t:
        t.next = ListNode(x)
        t = t.next
    else:
        t = ListNode(x)
        start = t

# s.print(start)
s.sortList(start)
