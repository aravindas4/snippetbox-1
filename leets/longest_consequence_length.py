class Solution:
	# @param A : tuple of integers
	# @return an integer
    def longestConsecutive(self, A):
        hset = set()
        ans = 0

        for ele in A:
            hset.add(ele)

        for ele in hset:
            if ele-1 not in hset:
                chain = 1
                next_ele = ele + 1

                while next_ele in hset:
                    chain += 1
                    next_ele += 1
                
                ans = max(ans, chain)

        return ans

s = Solution()
A = [100,4,200,1,3,2]
print(s.longestConsecutive(A))