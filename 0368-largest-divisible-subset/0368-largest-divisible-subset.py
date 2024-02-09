class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        dp1 = [1 for _ in range(len(nums))]
        dp2 = defaultdict(lambda: -1)
        maxLen = 1
        maxInd = 0
        for i, val in enumerate(nums):
            for j in range(i - 1, -1, -1):
                if val % nums[j] == 0 and dp1[j] + 1 > dp1[i]:
                    dp1[i] = dp1[j] + 1
                    dp2[i] = j
                    if dp1[i] > maxLen:
                        maxLen = dp1[i]
                        maxInd = i
        res = []
        while maxInd > -1:
            res.append(nums[maxInd])
            maxInd = dp2[maxInd]
        return res