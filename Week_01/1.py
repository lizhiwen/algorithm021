class Solution:
    def twoSum(self,nums,target):
        tmp = {}
        for i,n in enumerate(nums):
            if target-n in tmp.keys():
                return [tmp[target-n],i]
            else:
                tmp[n] = i
            