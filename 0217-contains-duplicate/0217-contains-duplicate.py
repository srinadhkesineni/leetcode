class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
      d={}
      for i in nums:
        if i in d:
          d[i]+=1
        if i not in d:
          d[i]=1
      for key , value in d.items():
        if value>1:
          return True
      return False


        
        