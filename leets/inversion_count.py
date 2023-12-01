class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        N = len(A)
        return self.countInversion(A, 0, N-1)


    def countInversion(self, A, l, r):
        ans = 0
        if l == r:
            return ans
        
        mid = (l+r) // 2

        ans += self.countInversion(A, l, mid)
        ans += self.countInversion(A, mid+1, r)

        ans += self.merge_arrays(A, l, mid, r)

        print(A)
        return ans

    def merge_arrays(self, A, l, mid, r):
        i = l
        j = mid + 1
        c = []
        count = 0
        print(l, r, mid)
        while i <= mid and j <= r:
            if A[i] <= A[j]:
                c.append(A[i])
                i += 1
            else:
                c.append(A[j])
                count += (mid - i + 1)
                j += 1
        
        # rr = 0
        while i <= mid:
            c.append(A[i])
            i += 1
            # rr += 1
            # count += 1

        # count = count * rr

        while j <= r:
            c.append(A[j])
            j += 1

        
        for ii in range(l, r+1):
            A[ii] = c[ii-l]

        return count

s = Solution()
A = [28,18,44,49,41,14]
print(s.solve(A))