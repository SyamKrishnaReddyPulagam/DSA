class Solution(object):
    def addDigits(self, num):
        def add(num):
            num=str(num)
            x=0
            for i in range(len(num)):
                x+=int(num[i])
            if(x>9):
                return add(x)
            else:
                return x
        a=add(num)
        return a