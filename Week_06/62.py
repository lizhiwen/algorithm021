
class Solution:
    def uniquePaths(self,m:int,n:int) -> int:
        print([1] * n)
        for _ in range(m-1):
            print([1]+[0]*(n-1))
            
        f = [[1] * n] + [[1] + [0] * (n - 1) for _ in range(m - 1)]
        for i in range(1, m):
            for j in range(1, n):
                f[i][j] = f[i - 1][j] + f[i][j - 1]
        
        return f[m-1][n-1]

if __name__ == '__main__':
    Solution().uniquePaths(3,7)