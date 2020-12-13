class Solution:
    def topKFrequent(self, nums, k):
        if not nums:
            return None
        count_dict = {}
        for n in nums:
            if n in count_dict.keys():
                continue
            count_dict[n] = {'number':n,'total':nums.count(n)}
        count_list = list(count_dict.values())
        count_list = sorted(count_list,key=lambda x:x['total'],reverse=True)
        ans = []
        for count_dict in count_list[:k]:
            ans.append(count_dict['number'])
        return ans