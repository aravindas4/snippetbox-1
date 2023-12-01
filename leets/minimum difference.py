# import sys

# class Solution:
#     # @param A : integer
#     # @param B : integer
#     # @param C : list of list of integers
#     # @return an integer
#     def solve(self, A, B, C):

#         for _r in C:
#             _r.sort()

#         ans = sys.maxsize

#         for ri in range(A-1):
#             row = C[ri]
#             for ele in row:
#                 ind = self.bs(0, B-1, ele, C[ri+1])

#                 if ind >=0 and ind < B:
#                     ans = min(ans, abs(ele - C[ri+1][ind]))
                
#                 if ind-1 >= 0 and ind-1 < B:
#                     ans = min(ans, abs(ele - C[ri+1][ind-1]))


#         return ans

#     def bs(self, l, r, tar, arr):
#         mid = l + (r - l) // 2

#         if arr[mid] == tar:
#             return mid
#         elif arr[mid] < tar:
#             l = mid + 1
#         else:
#             r = mid - 1
        
#         return l


# # import sys

# # class Solution:
# #     # @param A : integer
# #     # @param B : integer
# #     # @param C : list of list of integers
# #     # @return an integer
# #     def solve(self, A, B, C):

# #         for _r in C:
# #             _r.sort()

# #         ans = sys.maxsize

# #         for ri in range(A-1):
# #             row = C[ri]
# #             for ele in row:
# #                 b = 0
# #                 l = 0
# #                 r = B - 1

# #                 # ans = B
# #                 # while l <= r:
# #                 #     mid = l + (r - l) // 2

# #                 #     mide = C[ri+1][mid]
# #                 #     if mide < ele:
# #                 #         l = mid + 1
# #                 #     else:
# #                 #         ans = mid
# #                 #         r = mid - 1

# #                 a = sys.maxsize
# #                 l = 0
# #                 r = B - 1
# #                 ai = B
# #                 while l <= r:
# #                     mid = l + (r - l) // 2
# #                     mide = C[ri+1][mid]
# #                     if mide >= ele:
# #                         # if mide < a:
# #                         #     a = mide 
# #                         #     ai = mid
# #                         # a = min(mide, a)
# #                         r = mid - 1
# #                     else:
# #                         l = mid + 1

# #                 if 0 <= ai - 1 < B:
# #                     b = C[ri+1][b]
                
# #                 ans = min(ans, min(a - ele, ele - b))

# #         return ans

import sys

class Solution:
    # @param A : integer
    # @param B : integer
    # @param C : list of list of integers
    # @return an integer
    def solve(self, A, B, C):

        for _r in C:
            _r.sort()

        ans = sys.maxsize

        for ri in range(A-1):
            row = C[ri]
            for ele in row:
                arr = C[ri+1]
                ind = self.bs(arr, ele)

                if ind != B:
                    ans = min(ans, abs(ele - arr[ind]))
                
                if ind != 0:
                    ans = min(ans, abs(ele - arr[ind-1]))

                print(ans)

        return ans

    def bs(self, arr, tar):
        l = 0
        h = len(arr) - 1
        ans = len(arr)

        while l <= h:
            mid = l + (h - l) // 2
            # print(mid)
            if arr[mid] < tar:
                l = mid + 1
            else:
                ans = mid
                h = mid - 1

        print(arr, tar, ans)
        return ans

s = Solution()
print(s.solve(3, 2, [[7,3],[2,1],[4,9]]))