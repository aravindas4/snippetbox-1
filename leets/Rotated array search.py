class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return an integer
    def search(self, A, B):
        N = len(A)
        arr = A
        l = 0
        r = N -1 

        
        if A[0] > A[N-1]:
            while l <= r:
                mid = l + (r-l) // 2

                if arr[mid] == B:
                    return mid

                if arr[0] > B:
                    if arr[mid] >= arr[0]:
                        l = mid + 1
                    else:
                        if arr[mid] <= B:
                            l = mid + 1
                        else:
                            r = mid - 1
                else:
                    if arr[mid] >= arr[0]:
                        if arr[mid] > B:
                            r = mid - 1
                        else:
                            l = mid + 1
                    else:
                        r = mid - 1
        else:
            while l <= r:
                mid = l + (r - l) // 2

                if arr[mid] == B:
                    return mid
                if arr[mid] < B:
                    l = mid + 1
                else:
                    r = mid - 1
        return -1 

S = Solution()
A = [ 5, 1, 3 ]
B = 5
print(S.search(A, B))