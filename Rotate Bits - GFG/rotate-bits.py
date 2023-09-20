#User function Template for python3

class Solution:
    def rotate(self, N, D):
        # code here
        D=D%16
        binary=format(N,'016b')
        left_ro=binary[D:]+binary[:D]
        right_ro = binary[-D:] + binary[:-D] 
        d_l=int(left_ro,2)
        d_r=int(right_ro,2)
        return [d_l,d_r]
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n, d = input().strip().split(" ")
        n, d = int(n), int(d)
        ob = Solution()
        ans = ob.rotate(n, d)
        print(ans[0])
        print(ans[1])
# } Driver Code Ends