class Solution(object):
    def maxScore(self, s):
        x,y,z=0,0,0
        for i in range(1,len(s)):
            x=s[:i].count('0')
            y=s[i:].count('1')
            z=max(z,x+y)
        return z