#User function Template for python3

from typing import List

class Solution:
    def makeBeautiful(self, arr: List[int]) -> List[int]:
        stack = []
        for num in arr:
            if not stack or (stack[-1] < 0 and num < 0) or (stack[-1] >= 0 and num >= 0):
                stack.append(num)
            else:
                stack.pop()
        return stack


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        
        n = int(input())
        
        arr = list(map(int,input().split()))
        
        obj = Solution()
        res = obj.makeBeautiful(arr)
        print(*res)
# } Driver Code Ends