class Solution:
    def isAnagram(self, s, t):
        if s == t:
            return True
        s_ord,t_ord = [0]*26,[0]*26
        for s1 in s:
            s_ord[ord(s1)-ord("a")] += 1
        for t1 in t:
            t_ord[ord(t1)-ord("a")] += 1
        return True if s_ord == t_ord else False
    
if __name__ == '__main__':
    S = Solution()
    print(S.isAnagram("anagram","nagaram"))