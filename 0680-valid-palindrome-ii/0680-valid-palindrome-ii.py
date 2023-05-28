class Solution(object):
    def validPalindrome(self, s):
        s1=s[::-1]
        if s==s1:
            return True
        x,y=0,len(s)-1
        while(x<y):
            if s[x]!=s[y]:
                i=s[x:y]
                j=s[x + 1:y + 1]
                return i==i[::-1] or j==j[::-1]
            x=x+1
            y=y-1
        return True