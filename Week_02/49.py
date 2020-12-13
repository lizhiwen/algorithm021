class Solution:
    def groupAnagrams(self, strs):
        def setOrd(s):
            r = [0]*26
            for s1 in s:
                r[ord(s1)-ord("a")] += 1
            return r
        ans = {}
        for s in strs:
            s_ord = json.dumps(setOrd(s))
            if s_ord not in ans.keys():
                ans[s_ord] = []
            ans[s_ord].append(s)
        return list(ans.values())