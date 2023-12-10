class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        l=len(matrix)
        p=len(matrix[0])
        ans=[[2]*l for _ in range(p)]
        for i in range(l):
            for j in range(p):
                ans[j][i]=matrix[i][j]
        return ans