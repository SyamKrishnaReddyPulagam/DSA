class Solution(object):
    def reverse(self, x):
        x=str(x)
        if x[0] == "-":
            x=x[1:]
            x=x[::-1]
            x='-'+x
        else:
            x=x[::-1]
        if int(x) >= -2147483648 and int(x)<= 2147483647:
            return int(x)
        else:
            return 0