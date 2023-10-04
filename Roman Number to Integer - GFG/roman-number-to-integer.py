#User function Template for python3

class Solution:
    def romanToDecimal(self, S): 
        # code here
        array={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        prev_val=0
        res=0
        for i in S[::-1]:
            curr_val=array[i]
            
            if curr_val < prev_val:
                res-=curr_val
            else:
                res+=curr_val
            
            prev_val=curr_val
        return res


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=='__main__':
    t = int(input())
    for _ in range(t):
        ob = Solution()
        S = input()
        print(ob.romanToDecimal(S))
# } Driver Code Ends