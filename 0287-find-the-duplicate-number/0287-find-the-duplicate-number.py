class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        d={}
        for i in nums:
            if i in d:
                return i
            else:
                d[i]=1
        # for value in d:
        #     if value >1:
        #         return value
        

        