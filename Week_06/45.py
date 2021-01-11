class Solution:
    def jump(self,nums) -> int:
        nl = len(nums)
        
        cur,step,next_max = 0,0,0
        
        for i,n in enumerate(nums):
            if i > cur:
                cur = next_max
                step += 1
            next_max = max(next_max,i+n)
            if next_max > nl-1:
                return step
        

print(Solution().jump([2,3,0,1,4]))