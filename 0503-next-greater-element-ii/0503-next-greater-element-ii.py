class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n=len(nums)
        result=[-1]*n
        stack=[]
        for i in range(2*n):
            curr_idx=i%n
            while stack and nums[curr_idx]>nums[stack[-1]]:
                prev_idx=stack.pop()
                result[prev_idx]=nums[curr_idx]
            stack.append(curr_idx)
        return result