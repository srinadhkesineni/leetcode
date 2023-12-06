#User function Template for python3
from collections import Counter
class Solution:
    
    #Function to find the minimum indexed character.
    def minIndexChar(self,Str, pat): 
        #code here
        c=Counter(pat)
        idx=float('inf')
        for i in c:
            if i in Str:
                idx=min(Str.index(i),idx)
        if idx!=float('inf'):
            return idx
        return -1
                


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import atexit
import io
import sys

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER

@atexit.register

def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        s=str(input())
        p=str(input())
        obj = Solution()
        ans = obj.minIndexChar(s,p)
        print(ans)
# } Driver Code Ends