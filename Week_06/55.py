class Solution:
    def canJump(self,nums) -> bool:
        max_index = 0
        for i,n in enumerate(nums):
            if max_index >= i and (i+n) > max_index:
                max_index = i+n
                print(max_index,i,n)
        print(i)
        return max_index >= i
    
    def canJump2(self,nums) -> bool:
        def isRight(index):
            n = nums[index]
            if n == 0 and index < (len(nums)-1):
                return False
            if (index+n) >= len(nums)-1:
                return True
            for i in range(1,n+1):
                if isRight(index+i) is True:
                    return True
            return False
        return isRight(0)
            
print(Solution().canJump([3,2,1,0,4]))