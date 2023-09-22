class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
      d={}
      for i in nums:
        if i in d:
          return True
        if i not in d:
          d[i]=1
      return False


        
        