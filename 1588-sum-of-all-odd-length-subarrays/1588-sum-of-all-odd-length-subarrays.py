class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        res=0
        k=1
        while k<=len(arr):
            for i in range(len(arr)-k+1):
                res+=sum(arr[i:i+k])
            k+=2
        return res
