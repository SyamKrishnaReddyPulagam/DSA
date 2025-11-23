class Solution:
    def sumAndMultiply(self, n: int) -> int:
        a,sums,power=0,0,0
        while n:
            rem=n%10
            if rem!=0:
                a=rem*(10**power)+a
                power+=1
            n=n//10
            sums+=rem
        print(a)
        return a*sums
            