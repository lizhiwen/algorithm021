class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        nums = [i for i in range(1,n+1)]
        res = []
        def backtrace(nums_b,curr_res,index):
            if len(curr_res)==k:
                res.append(curr_res[:])
                return 
            for i in range(index,n):
                curr_res.append(nums[i])
                backtrace(nums_b[index:],curr_res,i+1)
                curr_res.pop()
        if n==0 or k==0:
            return res
        backtrace(nums,[],0)
        return res