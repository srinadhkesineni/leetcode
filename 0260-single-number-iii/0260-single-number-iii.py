class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        d={}
        a=[]
        for i in nums:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        for key,value in d.items():
            if value==1:
                a.append(key)
        return a
        