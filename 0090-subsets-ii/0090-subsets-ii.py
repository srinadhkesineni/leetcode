class Solution(object):
    


    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        total=[]
        ds=[]
        def func(idx,arr,ds):
            if idx==len(arr):
                total.append(ds[:])
                return
            ds.append(arr[idx])
            func(idx+1,arr,ds)
            ds.pop(-1)
            while idx+1 <len(arr) and nums[idx]==nums[idx+1]:
                idx+=1
            func(idx+1,arr,ds)
            return 
        nums.sort()
        func(0,nums,ds)
        return total
            

        