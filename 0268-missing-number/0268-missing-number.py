class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        s=sum(nums)
        n=len(nums)
        totalSum=(n*(n+1))/2
        return int(totalSum-s)