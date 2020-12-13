class Solution:
    def getLeastNumbers(self, arr, k):
        if len(arr) < k:
            return False
        if len(arr) == k:
            return arr
        arr = sorted(arr)
        return arr[:k]