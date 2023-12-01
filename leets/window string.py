class Solution:
	# @param A : string
	# @param B : string
	# @return a strings
    def compare(self, fa, fb):
        N = len(fa)

        for i in range(N):
            if fa[i] < fb[i]:
                return False
        return True
    
    def minWindow(self, A, B):
        fa = [0 for _ in range(75)]
        fb = [0 for _ in range(75)]
        N = len(A)
        M = len(B)
        ans = N
        si = N

        def get_idx(char):
            return ord(char) - ord('0')



        if M > N:
            return ''

        for i in range(M):
            fa[get_idx(A[i])] += 1
            fb[get_idx(B[i])] += 1

        # if self.compare(fa, fb):
        #     if M < ans:
        #         ans = M 
        #         si = 0
        # print(fa, fb)
        l = 0
        r = M-1
        
        while r < N:
            if self.compare(fa, fb):
                print((r - l + 1), ans, si)
                if (r - l + 1) < ans:
                    ans = r - l + 1
                    si = l
                elif (r - l + 1) == ans:
                    si = min(si, l)
                fa[get_idx(A[l])] -= 1
                l += 1
            else:
                r += 1
                if r == N: 
                    break
                fa[get_idx(A[r])] += 1
                
        if si == N:
            return ''
        
        return A[si: si + ans]
            
s = Solution()
print(s.minWindow('A', 'A'))
print(s.minWindow('ADOBECODEBANC', 'ABC'))
A = 'xiEjBOGeHIMIlslpQIZ6jERaAVoHUc9Hrjlv7pQpUSY8oHqXoQYWWll8Pumov89wXDe0Qx6bEjsNJQAQ0A6K21Z0BrmM96FWEdRG69M9CYtdBOrDjzVGPf83UdP3kc4gK0uHVKcPN4HPdccm9Qd2VfmmOwYCYeva6BSG6NGqTt1aQw9BbkNsgAjvYzkVJPOYCnz7U4hBeGpcJkrnlTgNIGnluj6L6zPqKo5Ui75tC0jMojhEAlyFqDs7WMCG3dmSyVoan5tXI5uq1IxhAYZvRQVHtuHae0xxwCbRh6S7fCLKfXeSFITfKHnLdT65K36vGC7qOEyyT0Sm3Gwl2iXYSN2ELIoITfGW888GXaUNebAr3fnkuR6VwjcsPTldQSiohMkkps0MH1cBedtaKNoFm5HbH15kKok6aYEVsb6wOH2w096OwEyvtDBTQwoLN87JriLwgCBBavbOAiLwkGGySk8nO8dLHuUhk9q7f0rIjXCsQeAZ1dfFHvVLupPYekXzxtWHd84dARvv4Z5L1Z6j8ur2IXWWbum8lCi7aErEcq41WTo8dRlRykyLRSQxVH70rUTz81oJS3OuZwpI1ifBAmNXoTfznG2MXkLtFu4SMYC0bPHNctW7g5kZRwjSBKnGihTY6BQYItRwLUINApd1qZ8W4yVG9tnjx4WyKcDhK7Ieih7yNl68Qb4nXoQl079Vza3SZoKeWphKef1PedfQ6Hw2rv3DpfmtSkulxpSkd9ee8uTyTvyFlh9G1Xh8tNF8viKgsiuCZgLKva32fNfkvW7TJC654Wmz7tPMIske3RXgBdpPJd5BPpMpPGymdfIw53hnYBNg8NdWAImY3otYHjbl1rqiNQSHVPMbDDvDpwy01sKpEkcZ7R4SLCazPClvrx5oDyYolubdYKcvqtlcyks3UWm2z7kh4SHeiCPKerh83bX0m5xevbTqM2cXC9WxJLrS8q7XF1nh'
B = 'dO4BRDaT1wd0YBhH88Afu7CI4fwAyXM8pGoGNsO1n8MFMRB7qugS9EPhCauVzj7h'
print(s.minWindow(A, B))
