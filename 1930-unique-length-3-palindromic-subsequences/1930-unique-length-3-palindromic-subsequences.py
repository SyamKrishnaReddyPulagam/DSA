class Solution(object):
    def countPalindromicSubsequence(self, s):
        count = 0
        chars = set(s)
        for c in chars:
            first, last = s.find(c), s.rfind(c)
            count += len(set(s[first + 1: last]))
        return count