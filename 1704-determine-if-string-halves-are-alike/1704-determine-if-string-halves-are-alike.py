class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        l=len(s)//2
        str1=s[:l]
        str2=s[l:]
        count1=0
        count2=0
        for i in str1:
            if i in 'aeiouAEIOU':
                count1+=1
        for i in str2:
            if i in 'aeiouAEIOU':
                count2+=1

        return count1==count2
        
