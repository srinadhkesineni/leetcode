class Solution:
    def kthSmallest(self, matrix: list[list[int]], k: int) -> int:
        matrix = [y for x in matrix for y in x]
        return sorted(matrix)[k - 1]