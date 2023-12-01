# Definition for singly-linked list.
# class ListNode:
#	def __init__(self, x):
#		self.val = x
#		self.next = None

class Solution:
	# @param A : head node of linked list
	# @return an integer
    def lPalin(self, A):
       sp = A
       fp = A 

       while fp.next and fp.next.next:
           sp = sp.next
           fp = fp.next.next

       
       h2 = sp.next
       sp.next = None

       h2 = self.reverse(h2)

       if self.compare(A, h2):
           ans = 1
       else:
           ans = 0

       h2 = self.reverse(h2)
       sp.next = h2
       # 5,66,68,42,73,25,84,63,72,20,77,38,8,99,92,49,74,45,30,51,50,95,56,19,31,26,98,67,100,2,24,6,37,69,11,16,61,23,78,27,64,87,3,85,55,22,33,62
       return ans


    def compare(self, h1, h2):
        c1 = h1
        c2 = h2 

        while c1 and c2:
            # print(c1.val, c2.val)
            if c1.val != c2.val:
                return False

            c1 = c1.next
            c2 = c2.next

        return True


    def reverse(self, H):
        p = None 
        c = H 

        while c != None:
            t = c.next
            c.next = p 
            p = c 
            c = t

        return p