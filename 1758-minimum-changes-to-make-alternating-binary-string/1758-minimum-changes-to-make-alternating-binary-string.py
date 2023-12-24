class Solution:
    def minOperations(self, s: str) -> int:
        n=len(s)
        if s[0]=="0":
            if n%2==0:
                s1="01"*(n//2)
            else:
                s1=("01"*(n//2))+"0"
        else:
            if n%2==0:
                s1="10"*(n//2)
            else:
                s1=("10"*(n//2))+"1"
        count=0
        for i in range(n):
            if s[i]!=s1[i]:
                count+=1
        return min(count,n-count)