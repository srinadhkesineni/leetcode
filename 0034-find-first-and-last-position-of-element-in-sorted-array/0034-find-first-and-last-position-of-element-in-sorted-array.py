class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l, r = 0, len(nums) - 1
        first, last = -1, -1

        while l <= r:
            m = (l + r) // 2

            if nums[m] == target:
                ms = m
                first, last = m, m

                while ms < len(nums) - 1 and nums[ms] == nums[ms + 1]:
                    last = ms+1
                    ms += 1

                ls = m
                while ls > 0 and nums[ls] == nums[ls - 1]:
                    first = ls-1
                    ls -= 1

                break

            elif nums[m] > target:
                r = m - 1

            elif nums[m] < target:
                l = m + 1

        return [first, last]
