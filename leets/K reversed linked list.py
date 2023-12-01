# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
    
    def __str__(self):
        return str(self.val)

class Solution:
	# @param A : head node of linked list
	# @param B : integer
	# @return the head node in the linked list
    def reverseList(self, A, B):
        head = A
        phead = None
        chead = head
        prev = None
        cur = head
        temp = None
        count = 0
        ahead = head
        
        while cur:
            prev = None
            temp = None
            print(prev, cur, temp)
            for i in range(B-1):
                temp = cur.next
                print(temp)
                cur.next = prev
                prev = cur
                cur = temp
            else:
                if phead:
                    phead.next = prev
                phead = chead
                chead = cur
                count += 1

                if count == 1:
                    ahead = prev

        return ahead
    


def ll(A):
    prev = None
    count = 0
    head = None
    for i in A:
        n = ListNode(i)
        count += 1
        
        if prev:
            prev.next = n

        if count == 1:
            head = n
        prev = n

    return head
    

s = Solution()
A = [8,11,4,12,0]
# print(ll(A))
print(s.reverseList(ll([8,11,4,12,0]), 1))
          