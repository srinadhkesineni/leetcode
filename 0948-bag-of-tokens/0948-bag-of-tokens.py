class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        tokens.sort()
        left=0
        right=len(tokens)-1
        score=0
        max_score=0
        while left<=right:
            if power>=tokens[left]:
                power-=tokens[left]
                score+=1
                max_score=max(score,max_score)
                left+=1
            elif score>0:
                score-=1
                power+=tokens[right]
                right-=1
            else:
                break
        return max_score