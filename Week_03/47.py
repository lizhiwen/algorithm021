class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        length, res = len(nums), []
        def helper(index):
            if index == length:
                res.append(list(nums))
                return
            visited = set()
            for i in range(index, length):
                if nums[i] in visited:
                    continue
                visited.add(nums[i])
                nums[i], nums[index] = nums[index], nums[i]
                helper(index+1)
                nums[i], nums[index] = nums[index], nums[i]
        helper(0)
        return res