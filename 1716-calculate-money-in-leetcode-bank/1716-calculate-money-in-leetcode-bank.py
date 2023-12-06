class Solution:
    def totalMoney(self, n: int) -> int:
        week=n//7
        ans=0
        for i in range(week):
            ans+=28+(i*7)
        remain=n%7
        if remain==0:
            return ans
        else:
            pre_week=week+1
            while remain>0:
                ans+=pre_week
                pre_week+=1
                remain-=1
        return ans
        