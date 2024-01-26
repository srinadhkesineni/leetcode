class Solution(object):
    def combinationSum(self, candidates, target):
        ans=[]
        ds=[]
        def poop(idx,target):
            if idx==len(candidates):
                if target==0:
                    ans.append(ds[:])
                return
            if candidates[idx]<=target:
                ds.append(candidates[idx])
                poop(idx,target-candidates[idx])
                ds.pop()
            poop(idx+1,target)
        poop(0,target)
        return ans
