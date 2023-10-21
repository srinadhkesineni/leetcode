#User function Template for python3

def isSubset( a1, a2, n, m):
    d={}
    for i in a1:
        if i in d:
            d[i]+=1
        else:
            d[i]=1
    for i in a2:
        if i in d and d[i]>0:
            d[i]-=1
        else:
            return "No"
    return "Yes"
    
            
    
    
    



#{ 
 # Driver Code Starts
#Initial Template for Python 3


def main():

    T = int(input())

    while(T > 0):
        sz = [int(x) for x in input().strip().split()]
        n, m = sz[0], sz[1]
        a1 = [int(x) for x in input().strip().split()]
        a2 = [int(x) for x in input().strip().split()]
        
        print(isSubset( a1, a2, n, m))

        T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends