class Solution:
	# @param A : integer
	# @return an integer
    def colorful(self, A):
        arr = []
        
        while A > 0:
            rem = A % 10
            arr.append(rem)
            A = A // 10

        N = len(arr)
        pprod = [0 for _ in range(N)]
        print(arr)
        print(pprod)
        pprod[0] = arr[0]

        for ind in range(1, N):
            pprod[ind] = pprod[ind-1] * arr[ind]

        hash_set = set()
        for i in range(N):
            for j in range(i, N):
                p = pprod[j]

                if i > 0:
                    p = p // pprod[i-1]
            
                if p not in hash_set:
                    hash_set.add(p)
                else:
                    return 0

        return 1

s = Solution()
A = 23
print(s.colorful(A))