class Solution:
    def findPrimePairs(self, n: int) -> List[List[int]]:
        if n<2:
            return []
        primes=[True for i in range(n)]
        for i in range(2,len(primes)):
            c=primes[i]
            if c:
                for j in range(i*i,n,i):
                    primes[j]=False
        ans=[]
        primes[0],primes[1]=False,False
        for i in range(2,(n//2)+1):
            if primes[i] and primes[n-i]:
                ans.append([i,n-i])
        return ans