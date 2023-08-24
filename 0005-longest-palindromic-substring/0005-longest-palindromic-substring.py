class Solution(object):
    def longestPalindrome(self, s):
        def helper(self, s, l, r):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1; r += 1
            return s[l+1:r]
        res = ""
        for i in xrange(len(s)):
            # odd case, like "aba"
            tmp = helper(self,s,i,i)
            if len(tmp) > len(res):
                res = tmp
            # even case, like "abba"
            tmp = helper(self,s, i, i+1)
            if len(tmp) > len(res):
                res = tmp
        return res
        
