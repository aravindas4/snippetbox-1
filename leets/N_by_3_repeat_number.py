class Solution:
    # @param A : tuple of integers
    # @return an integer
    def repeatedNumber(self, A):
        N = len(A)
        candidate_1 = -1
        candidate_2 = -1
        count_1 = 0
        count_2 = 0

        for ind in range(0, N):
            if A[ind] == candidate_1:
                count_1 += 1
            elif A[ind] == candidate_2:
                count_2 += 1
            elif count_1 == 0:
                candidate_1 = A[ind]
                count_1 += 1
            elif count_2 == 0:
                candidate_2 = A[ind]
                count_2 += 1
            else:
                count_1 -= 1
                count_2 -= 1

        count_1 = 0
        count_2 = 0

        for num in A:
            if num == candidate_1:
                count_1 += 1
            elif num == candidate_2:
                count_2 += 1

        if count_1 > N / 3:
            return candidate_1
        elif count_2 > N / 3:
            return candidate_2
        
        return -1

    

s = Solution()
print(s.repeatedNumber([1,1,1,2,3,5,7]))