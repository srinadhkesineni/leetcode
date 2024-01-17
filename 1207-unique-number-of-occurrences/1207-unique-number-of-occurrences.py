class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        c=Counter(arr)
        s=set()
        for key,val in c.items():
            if val in s:
                return False
            else:
                s.add(val)
        return True
