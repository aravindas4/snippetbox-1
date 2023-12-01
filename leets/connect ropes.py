import sys

class Heap:
    
    def __init__(self, arr=None):
        if arr is None:
            arr = []

        self.arr = arr

    def insert(self, val):
        self.arr.append(val)
        i = len(self.arr) - 1

        while i > 0:
            p = (i-1) // 2

            if self.arr[p] > self.arr[i]:
                self.arr[i], self.arr[p] = self.arr[p], self.arr[i]
                i = p
            else:
                break

    def getMin(self):
        ans = self.arr[0]
        self.arr[0] = self.arr[-1]
        self.arr.pop()

        if self.leng() > 1:
            self.heapify(0)
        # print("get_min", ans, self.arr)
        return ans

    def leng(self):
        return len(self.arr)

    def heapify(self, ind):
        i = ind
        N = len(self.arr)
        int_max = sys.maxsize

        while i < N:
            # print("OOO", self.arr, i)
            li = 2 * i + 1
            ri = 2 * i + 2
            if li < N:
                lv = self.arr[li]
            else:
                lv = int_max

            if ri < N:
                rv = self.arr[ri]
            else:
                rv = int_max

            # print(f"[{li}] = {lv}", f"[{ri}] = {rv}")
            min_val = min(lv, rv)

            if lv <= rv:
                min_ind = li
            else:
                min_ind = ri

            print(f"min_ind={min_ind}", f"min_val={min_val}", f"arr[{i}]={self.arr[i]}")
            if self.arr[i] >= min_val:
                # print("swapped")
                self.arr[i], self.arr[min_ind] = self.arr[min_ind], self.arr[i]
                i = min_ind
            else:
                break


def build(arr):
    h = Heap(arr)
    N = len(arr)
    idx = (N - 1) // 2
    print("idx", idx)
    for i in range(idx, -1, -1):
        print(f"heapfiy:{i} out of {idx}")
        h.heapify(i)
        

    return h


class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        h = build(A)
        print(h.arr)
        ans = 0

        while h.leng() > 1:
            val1 = h.getMin()
            val2 = h.getMin()
            val = val1 + val2
            ans += val
            h.insert(val)
            # print("HHH", h.arr, val)
            # break
        return ans

s = Solution()
# A = [1, 2, 3, 4, 5]
# A = [55,96,84,70,11,27,29,165,91,54,71,134,131,44,70,39,151,64,2,160,10,82,26,146,23,19,26,89,24,14,198,53,85,162]
# A = [5, 17, 100, 11]
A = [1,18]
print(s.solve(A))