class Solution:
    def commonFactors(self, a: int, b: int) -> int:
        z=min(a,b)
        count=1
        for i in range(2,z+1):
            if a%i==0 and b%i==0:
                count+=1
        return count