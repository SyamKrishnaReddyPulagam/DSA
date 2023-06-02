class Solution(object):
    def addBinary(self, a, b):
        a=int(a,2)
        b=int(b,2)
        return bin(a+b).replace("0b","")