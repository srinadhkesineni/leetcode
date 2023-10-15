#User function Template for python3

class Solution:
    #Function to return the position of the first repeating element.
    def firstRepeated(self,arr, n):
        
        #arr : given array
        #n : size of the array
        d = {}  # Dictionary to store the first occurrence index of elements
        min_index = n  # Initialize min_index to a value equal to the array size
    
        for i in range(n - 1, -1, -1):
            if arr[i] in d:
                min_index = i
            else:
                d[arr[i]] = i
    
        if min_index < n:
            return min_index + 1  
        else:
            return -1

#{ 
 # Driver Code Starts
#Initial Template for Python 3

#contributed by RavinderSinghPB
if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        n=int(input())
        
        arr=[int(x) for x in input().strip().split()]
        ob = Solution()
        print(ob.firstRepeated(arr, n))
# } Driver Code Ends