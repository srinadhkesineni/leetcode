class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        d={}
        for i in s:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        for j in t:
            if j in d:
                d[j]-=1
                if d[j]==0:
                    del d[j]
            else:
                return j
        # for k,v in d.items():
        #     if v==1:
        #         return k
            