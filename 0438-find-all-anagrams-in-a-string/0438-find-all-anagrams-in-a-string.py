class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        c1=Counter(p)
        l=[]
        for i in range(len(s)-len(p)+1):
            r=s[i:i+len(p)]
            c2=Counter(r)
            if c1==c2:
                l.append(i)
        return l