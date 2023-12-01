from functools import cmp_to_key

class Solution:
    # @param A : tuple of integers
    # @return a strings
    def largestNumber(self, A):
        A = [str(i) for i in A]
        A.sort(key=cmp_to_key(self.custom_cmp))
        return "".join(A)

    def custom_cmp(elf, a, b):
        A = a
        B = b

        l = min(len(A), len(B))
        if len(A) > len(B):
            lar = A
        else:
            lar = B
        
        print("l:", l, "A:", A, "B:", B)
        for ind in range(l):
            if A[ind] > B[ind]:
                return -1
            elif A[ind] < B[ind]:
                return 1
        return 
    
s = Solution()
print(s.largestNumber([3,30,34,5,9]))