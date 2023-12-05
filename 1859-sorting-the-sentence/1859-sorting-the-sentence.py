class Solution:
    def sortSentence(self, s: str) -> str:
        a=s[::-1].split()
        a.sort()
        l=[]
        for word in a:
            l.append(word[1:][::-1])
        return " ".join(l)

        
        
