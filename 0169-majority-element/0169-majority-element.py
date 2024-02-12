class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        c=Counter(nums)
        n=len(nums)/2
        for k,v in c.items():
            if v>n:
                return k
        return 0