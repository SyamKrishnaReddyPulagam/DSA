class Solution:
    def countBits(self, n: int) -> List[int]:
        if n==0:
            return [n]
        def func(n):
            count=0
            while n:
                if n&1==1:
                    count+=1
                n>>=1
            return count
        arr=[0]*(n+1)
        arr[1]=1
        for i in range(2,n+1):
            arr[i]=func(i)
        return arr