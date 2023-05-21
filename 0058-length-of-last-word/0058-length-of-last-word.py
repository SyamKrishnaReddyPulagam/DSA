class Solution(object):
    def lengthOfLastWord(self, s):
        s=s.split()
        s=s[-1]
        s=len(s)
        return s
        