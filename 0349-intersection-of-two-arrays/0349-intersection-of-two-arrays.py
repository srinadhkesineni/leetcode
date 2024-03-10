class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        d={}
        s=set(nums1)
        s2=set(nums2)
        l=[]
        for i in s:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        for i in s2:
            if i in d:
                l.append(i)
        return l
        