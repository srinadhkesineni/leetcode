class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        n,ans=len(startTime),0
        state=[]
        for i in range(n):
            state.append([endTime[i],startTime[i],profit[i]])
        state=sorted(state)
        dp=[0 for i in range(n)]
        dp[0]=state[0][2]
        for i in range(1,n):
            prevIndex=bisect.bisect_left(state,[state[i][1]+1])
            if prevIndex==0:
                dp[i]=max(dp[i-1],state[i][2])
            else:
                dp[i]=max(dp[i-1],dp[prevIndex-1]+state[i][2])
            ans=max(ans,dp[i])
        return ans
                
                
                
