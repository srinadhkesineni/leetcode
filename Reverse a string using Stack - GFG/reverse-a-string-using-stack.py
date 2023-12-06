#{ 
 # Driver Code Starts

# } Driver Code Ends
def reverse(S):
    
    #Add code here
    stack=[]
    for i in S:
        stack.append(i)
    p=""
    while len(stack)>0:
        p+=stack.pop()
    return p
        
        

#{ 
 # Driver Code Starts.
if __name__=='__main__':
    t=int(input())
    for i in range(t):
        str1=input()
        print(reverse(str1))
# } Driver Code Ends