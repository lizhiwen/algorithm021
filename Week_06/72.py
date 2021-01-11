
class Solution:
    def minDistance(self,word1,word2) -> int:
        n = len(word1)
        m = len(word2)
        if n == 0 or m == 0:
            return m+n
        
        dp = [[0]*(m+1) for _ in range(n+1)]
        #边界初始化
        for i in range(n+1):
            dp[i][0] = i
        for j in range(m+1):
            dp[0][j] = j
        
        for i in range(1,n+1):
            for j in range(1,m+1):
                delete = dp[i-1][j] + 1
                add = dp[i][j-1] + 1
                modify = dp[i-1][j-1]
                if word1[i-1] != word2[j-1]:
                    modify += 1
                dp[i][j] = min(add,modify,delete)
        return dp[n][m]
                
        
Solution().minDistance('horse','ros')