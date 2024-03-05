class Solution:
    def minimumLength(self, s: str) -> int:
        n=len(s)
        if n==1:
            return 1
        if n>2 and s=="a"*n or s=="b"*n or s=="c"*n:
            return 0
        i,j=0,n-1
        while i<j:
            if s[i]==s[j]:
                c=s[i]
                while s[i]==c:
                    i+=1
                while s[j]==c:
                    j-=1
            else:
                break
        if j<i:
            return 0
        elif j==i:
            return 1
        else:
            return len(s[i:j+1])