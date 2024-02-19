class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        h=31
        for i in range(h):
            if pow(2,i)==n:
                return True
        return False