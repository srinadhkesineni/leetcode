class Solution:
    def trimMean(self, arr: List[int]) -> float:
        arr.sort()
        deletions=len(arr)/20
        while deletions>0:
            arr.pop()
            arr=arr[1:]
            deletions-=1
        return sum(arr)/len(arr)