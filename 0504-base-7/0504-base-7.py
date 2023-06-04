class Solution(object):
    def convertToBase7(self, num):
        a=num
        num=abs(num)
        rem=""
        quo=0
        while num>=7:
            rem+=str(num%7)
            num=num//7
        quo=num
        if a<0:
            return "-"+str(quo)+str(rem)[::-1]
        return str(quo)+str(rem)[::-1]