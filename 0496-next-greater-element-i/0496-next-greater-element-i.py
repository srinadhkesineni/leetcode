class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack=[]
        result=[]
        next_greater={}
        for num in nums2:
            while stack and stack[-1]<num:
                next_greater[stack.pop()]=num
            stack.append(num)
        for num in stack:
            next_greater[num]=-1
        for num in nums1:
            result.append(next_greater.get(num))
        return result
            
