class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        
        while left < right:
            mid = left + (right - left) // 2
            
            # Ensure mid is even
            if mid % 2 == 1:
                mid -= 1
            
            # If the single element is on the right side, update the left pointer
            if nums[mid] == nums[mid + 1]:
                left = mid + 2
            else:
                right = mid
            
        return nums[left]








        
        