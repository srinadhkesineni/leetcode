class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        d={}
        for i in s1:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        for i in range(len(s2)-len(s1)+1):
            r=s2[i:i+len(s1)]
            co=Counter(r)
            if d==co:
                return True
        return False
