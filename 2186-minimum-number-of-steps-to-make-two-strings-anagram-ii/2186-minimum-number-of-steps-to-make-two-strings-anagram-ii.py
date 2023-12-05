class Solution:
    def minSteps(self, s: str, t: str) -> int:
        s_counter=Counter(s)
        t_counter=Counter(t)

        diff=sum(abs(s_counter[c]-t_counter[c])for c in set(s+t))
        return diff
                    
                
