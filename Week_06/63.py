
class Solution:
    def uniquePathsWithObstacles(self,obstacleGrid) -> int:
        row,cols = len(obstacleGrid),len(obstacleGrid[0])
        
        res = [[0]*cols for _ in range(row)]
        
        for i in range(0, row):
            for j in range(0, cols):
                if obstacleGrid[i][j] == 1:
                    continue
                if i== 0 or j == 0:
                    res[i][j] = 1
                else:
                    res[i][j] = res[i-1][j] + res[i][j-1]
        return res[row-1][cols-1]

if __name__ == '__main__':
    print(Solution().uniquePathsWithObstacles([[0,0]]))