class Solution(object):
    def findContentChildren(self, g, s):
        i,j,x=0,0,0
        g.sort()
        s.sort()
        while(i<len(g) and j<len(s)):
            if(s[j]>=g[i]):
                i+=1
                x+=1
            j+=1
        if(i>len(s)):
            return len(s)
        return x