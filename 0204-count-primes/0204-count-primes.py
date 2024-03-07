class Solution:
    def countPrimes(self, n: int) -> int:
        if n<2:
            return 0
        prime=[True for i in range(n)]
        for i in range(2,n):
            c=prime[i]
            if c:
                for j in range(i+i,n,i):
                    prime[j]=False
        return prime.count(True)-2