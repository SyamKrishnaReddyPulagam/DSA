class Solution(object):
    def backspaceCompare(self, s, t):
        s1=""
        for i in s:
            if i.isalpha():
                s1+=i
            else:
                if s1:
                    s1=s1[:-1]
        t1=""
        for i in t:
            if i.isalpha():
                t1+=i
            else:
                if t1:
                    t1=t1[:-1]
        return s1==t1