class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        l=[]
        d={}
        for i in nums1:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        for j in nums2:
            if j in d:
                if d[j]>=1:
                    l.append(j)
                    d[j]-=1
        return l