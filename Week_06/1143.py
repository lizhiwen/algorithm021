class Solution:
    def longestCommonSubsequeue(self,text1,text2) -> int:
        if text1 == text2:
            return len(text1)
        def dp(i,j):
            if i < 0 or j < 0:
                return 0
            if text1[i] == text2[j]:
                print(text1[i],text2[j],dp(i-1,j-1))
                return dp(i-1,j-1)+1
            else:
                return max(dp(i-1,j),dp(i,j-1))
        return dp(len(text1)-1,len(text2)-1)

    def other(self,text1,text2) -> int:
        m,n = len(text1),len(text2)
        #初始化DP
        dp = [[0]*(n+1) for _ in range(m+1)]
        print(dp)
        for i in range(1,m+1):
            for j in range(1,n+1):
                print(text1[i-1],text2[j-1])
                if text1[i-1] == text2[j-1]:
                    dp[i][j] = 1+dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i-1][j],dp[i][j-1])
        return dp[-1][-1]

if __name__ == '__main__':
    print(Solution().longestCommonSubsequeue('abcde','ace'))