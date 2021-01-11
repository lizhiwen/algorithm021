import math

class Solution(object):
    def numSquare(self,n):
        lst = [i**2 for i in range(1,int(math.sqrt(n))+1)]
        print(lst)
        dp = [0] * (n+1)
        for num in range(1,n+1):
            min_n = num
            for j in [c for c in lst if c <= num]:
                if dp[num-j] + 1 < min_n:
                    min_n = dp[num-j] + 1
            dp[num] = min_n
        return dp[n]
        
if __name__ == '__main__':
    Solution().numSquare(12)