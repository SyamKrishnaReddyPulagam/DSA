class Solution:
    def countPrimes(self, n: int) -> int:
        if n<2:
            return 0
        prime=[True for i in range(n)]
        i=2
        while i*i<n:
            if prime[i]:
                for j in range(i*i,n,i):
                    prime[j]=False
            i+=1
        return prime.count(True)-2