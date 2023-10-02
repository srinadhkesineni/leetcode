#User function Template for python3

class Solution:
    def smallestSubstring(self, S):
        # Code here
        if '0' not in S:
            return -1
        arr = [-1, -1, -1]
        res = len(S)
        for i in range(len(S)):
            arr[int(S[i])] = i
            start = min(arr)
            end = max(arr)
            
            if start != -1:
                res = min(res, end-start+1)
        
        if start == -1:
            return -1
        return res


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	t=int(input())
	for i in range(t):
		S = input()
		ob = Solution()
		ans = ob.smallestSubstring(S)
		
		print(ans)



# } Driver Code Ends