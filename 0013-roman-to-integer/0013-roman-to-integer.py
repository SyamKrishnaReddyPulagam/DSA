class Solution(object):
    def romanToInt(self, s):
        dict={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        a=0
        s = s.replace("IV", "IIII").replace("IX", "VIIII")
        s = s.replace("XL", "XXXX").replace("XC", "LXXXX")
        s = s.replace("CD", "CCCC").replace("CM", "DCCCC")
        for i in s:
            a+=dict[i]
        return a