class Solution:
    def rotate(self, nums, k):
        """
        Do not return anything, modify nums in-place instead.
        """
        lenth = len(nums)
        nums[:] = nums[lenth-k:]+nums[:lenth-k]
        return nums
    
if __name__=='__main__':
    S = Solution()
    S.rotate([1,2,3,4,5,6,7],3)