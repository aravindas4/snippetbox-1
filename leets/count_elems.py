class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        max_num = 0

        count = 0

        # for num in A:
        #     if num > max_num:
        #         max_num = num 
        
        # for num in A:
        #     if num < max_num:
        #         count += 1

        for num in A:
            if max_num < num:
                max_num = num
                count = 1
            elif max_num == num:
                count +=1

        return len(A) - count


s = Solution()
print(s.solve([ 7, 4, 2, 10, 5 ]))