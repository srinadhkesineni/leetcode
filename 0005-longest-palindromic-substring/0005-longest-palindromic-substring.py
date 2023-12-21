class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s)<=1:
            return s
        max_count=1
        max_string=s[0]
        for i in range(len(s)-1):
            for j in range(i+1,len(s)):
                if max_count<j-i+1 and s[i:j+1]==s[i:j+1][::-1]:
                    max_count=j-i+1
                    max_string=s[i:j+1]
        return max_string
