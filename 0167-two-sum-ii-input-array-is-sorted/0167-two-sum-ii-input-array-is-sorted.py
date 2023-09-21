class Solution:
    def twoSum(self, k: List[int], target: int) -> List[int]:
        l,r=0,len(k)-1
        while l<r:
            curSum=k[l]+k[r]
            if curSum>target:
                r-=1
            elif curSum<target:
                l+=1
            else:
                return [l+1,r+1]