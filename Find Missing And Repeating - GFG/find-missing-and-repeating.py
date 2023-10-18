#User function Template for python3

class Solution:
    def findTwoElement( self,arr, n): 
        # code here
        arr.sort()
        d={}
        a=[]
        for i in range(n):
            if arr[i] in d:
                a.append(arr[i])
            else:
                d[arr[i]]=1
        for i in range(1,n+1):
            if i not in d:
                a.append(i)
                break
        return a
            


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 

    tc=int(input())
    while tc > 0:
        n=int(input())
        arr=list(map(int, input().strip().split()))
        ob = Solution()
        ans=ob.findTwoElement(arr, n)
        print(str(ans[0])+" "+str(ans[1]))
        tc=tc-1
# } Driver Code Ends