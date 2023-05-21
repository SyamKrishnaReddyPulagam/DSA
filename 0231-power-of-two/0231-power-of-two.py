class Solution(object):
    def isPowerOfTwo(self, n):
        if n==1:
            return True
        if n%2!=0:
            return False
        else:
            for i in range (31):
                if n==2**i:
                    return True
            return False
            