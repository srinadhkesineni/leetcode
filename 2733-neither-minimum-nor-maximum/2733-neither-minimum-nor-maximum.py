class Solution:
    def findNonMinOrMax(self, nums: List[int]) -> int:
        if len(nums)<=2:
            return -1
        nums.sort()
        for i in range(len(nums)):
            return nums[1]
        