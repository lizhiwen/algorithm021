class Solution:
    def removeDuplicates(self, nums):
        new = 0
        for i,v in enumerate(nums):
            if i == 0 or v != nums[i-1]:
                nums[new] = nums[i]
                new += 1
        return new
    
if __name__=='__main__':
    S = Solution()
    print(S.removeDuplicates([1,1,2]))