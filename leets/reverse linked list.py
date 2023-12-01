# Definition for singly-linked list.
class ListNode:
	def __init__(self, x):
		self.val = x
		self.next = None

class Solution:
	# @param A : head node of linked list
	# @return the head node in the linked list
    def get_val(self, l):
         return getattr(l, 'val', None)
    
    def reverseList(self, A):
        p = None
        c = A
        t = None
        while c != None:
            print(self.get_val(p), self.get_val(c), self.get_val(t))
            t = c.next
            c.next = p
            p = c
            if t:
                t.next = c
            c = t
        return p

s = Solution()
l = [97,63,89,34,82,95,4,70,14,41,38,83,49,32,68,56,99,52,33,54]

# print(s.reverseList())

def pop(l):
    c = None
    p = None

    for i in l:
        if c is None:
            c = ListNode(i)
            p = c
        else:
            c.next = ListNode(i)
            c = c.next

    return p

print(s.reverseList(pop(l)))   

