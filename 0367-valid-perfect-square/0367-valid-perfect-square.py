class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num==1:
            return True
        num_div_2=num//2
        l,r=0,num_div_2
        while l<=r:
            m=(l+r)//2
            square=m*m
            if square>num:
                r=m-1
            elif square<num:
                l=m+1
            elif square==num:
                return True
        return False
            
            
            

        