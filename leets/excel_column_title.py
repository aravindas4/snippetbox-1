class Solution:
	# @param A : integer
	# @return a string
    def convertToTitle(self, A):
        a = ord("A")
        arr = [chr(a + i) for i in range(26)]
        print(arr[0], arr[-1])
        o = ""
        A = A - 1
        while A > -1:
            rem = A % 26
            # print(rem)
            o = arr[rem] + o 
            A = (A // 26) - 1

        return o

s = Solution()
print(s.convertToTitle(1000))
