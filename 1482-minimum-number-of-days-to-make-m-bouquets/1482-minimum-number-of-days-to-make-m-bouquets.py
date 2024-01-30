class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        def possible(arr,day,m,k):
            count=0
            noOfB=0
            n=len(arr)
            for i in range(n):
                if arr[i]<=day:
                    count+=1
                else:
                    noOfB+=count//k
                    count=0
            noOfB+=count//k
            return noOfB>=m
        if len(bloomDay)<m*k:
            return -1
        low=min(bloomDay)
        high=max(bloomDay)
        while low<=high:
            mid=(low+high)//2
            if possible(bloomDay,mid,m,k):
                high=mid-1
            else:
                low=mid+1
        return low

        