class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        startingRow=0
        endingRow=n-1
        startingCol=0
        endingCol=n-1
        count=1
        total=n*n
        result=[[0 for _ in range(n)] for _ in range(n)]
        while count<=total:
            for i in range(startingCol,endingCol+1):
                result[startingRow][i]=count
                count+=1
            startingRow+=1
            for i in range(startingRow,endingRow+1):
                result[i][endingCol]=count
                count+=1
            endingCol-=1
            for i in range(endingCol,startingCol-1,-1):
                result[endingRow][i]=count
                count+=1
            endingRow-=1
            for i in range(endingRow,startingRow-1,-1):
                result[i][startingCol]=count
                count+=1
            startingCol+=1

        return result 

