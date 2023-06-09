class Solution(object):
    def maxNumberOfBalloons(self, text):
        a=text.count('b')
        b=text.count('a')
        c=(text.count('l'))//2
        d=(text.count('o'))//2
        e=text.count('n')
        return min(a,b,c,d,e)
            