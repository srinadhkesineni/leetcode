class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        mydict = {}
        for i in set(arr):
            mydict[arr.count(i)] = i
        return mydict[max(mydict)]
        
