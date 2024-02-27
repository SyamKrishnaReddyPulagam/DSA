class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        if a|b==c:
            return 0
        a,b,c=list(bin(a).replace("0b","")),list(bin(b).replace("0b","")),list(bin(c).replace("0b",""))
        a=[int(i) for i in a]
        b=[int(i) for i in b]
        c=[int(i) for i in c]
        len1=max(len(a),len(b),len(c))
        if len(a)!=len1:
            a=([0]*(len1-len(a)))+a
        if len(b)!=len1:
            b=([0]*(len1-len(b)))+b
        if len(c)!=len1:
            c=([0]*(len1-len(c)))+c
        ans=0
        for i in range(len1-1,-1,-1):
            if a[i] | b[i]==c[i]:
                continue
            else:
                if c[i]==1:
                    ans+=1
                else:
                    if a[i]==1 and b[i]==1:
                        ans+=2
                    elif a[i]==1 or b[i]==1:
                        ans+=1
        return ans
