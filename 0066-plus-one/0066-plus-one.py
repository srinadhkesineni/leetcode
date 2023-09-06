class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits = int("".join(map(str, digits))) + 1
        return [int(i) for i in str(digits)]
        