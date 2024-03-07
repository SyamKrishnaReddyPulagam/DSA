class Solution(object):
    def findPrimePairs(self, n):
        if n < 4:
            return []  
        primes=[True for i in range(n)]
        for i in range(2,len(primes)):
            c=primes[i]
            if c:
                for j in range(i*i,n,i):
                    primes[j]=False
        if n%2 or n == 4:                          
            return [[2,n-2]] if primes[n-2] else [] 
        return [[i, n - i] for i in range(3,(n+3)//2) if primes[i] and primes[n - i]]