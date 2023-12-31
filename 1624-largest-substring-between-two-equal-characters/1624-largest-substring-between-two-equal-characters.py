class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        d={}
        res=-1
        for i in range(len(s)):
            if s[i] in d:
                res=max(res,i-d[s[i]]-1)
            else:
                d[s[i]]=i
        return res
        
                