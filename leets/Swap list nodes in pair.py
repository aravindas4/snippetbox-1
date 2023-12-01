class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
          
    def __str__(self):
        return str(self.val)
    
    @classmethod
    def pprint(cls, node):
        temp = node

        while temp:
            print(str(temp.val) + '->', end='')
            temp = temp.next

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
    
class Solution:
	# @param A : head node of linked list
	# @return the head node in the linked list
    def swapPairs(self, A):
        c1 = A
        c2 = A.next
        prev = None

        if c2:
            head = c2
        else:
            head = c1

        while c2:
            # import pdb; pdb.set_trace()
            print(prev, c1, c2)
            c1.next = c2.next
            c2.next = c1
            if prev:
                prev.next = c2
            prev = c1
            c1 = c1.next
            if c1 and c1.next:
                c2 = c1.next
            else:
                c2 = None

            

        return head


s = Solution()
A = [8,11,4,12,0]
# print(ll(A))
ListNode.pprint(s.swapPairs(ll([1])))