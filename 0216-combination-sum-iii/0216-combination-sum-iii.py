class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        total=[]
        arr=[1,2,3,4,5,6,7,8,9]
        ds=[]
        def func(idx,nums,ds):
            if idx==9:
                if len(ds)==k:
                    if sum(ds)==n:
                        total.append(ds.copy())
                return
            if len(ds)==k:
                if sum(ds)==n:
                    total.append(ds.copy())
                return 
            ds.append(arr[idx])
            func(idx+1,nums,ds)
            ds.pop()
            func(idx+1,nums,ds)
            return             
        func(0,arr,ds)
        return total