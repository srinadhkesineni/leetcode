#User function Template for python3
class Solution:
	def addBinary(self, A, B):
		# code here
		int_a=int(A,2)
		int_b=int(B,2)
		s=int_a+int_b
		return bin(s)[2:]


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		a,b = input().split(" ")
		ob = Solution()
		answer = ob.addBinary(a,b)
		
		print(answer)


# } Driver Code Ends