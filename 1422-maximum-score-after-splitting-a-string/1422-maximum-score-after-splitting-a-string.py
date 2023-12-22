class Solution:
    def maxScore(self, s: str) -> int:
        ones = s.count('1')
        result = []
        for i in range(1,len(s)):
            result.append(s[:i].count('0')+(ones-(i-s[:i].count('0'))))
        return max(result)