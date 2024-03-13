class Solution:
    def pivotInteger(self, n: int) -> int:
        x=sqrt(n*(n+1)/2)
        if x==int(x):
            return int(x)
        return -1