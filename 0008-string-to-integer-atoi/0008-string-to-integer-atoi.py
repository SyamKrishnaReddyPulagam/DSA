class Solution:
    def myAtoi(self, s: str) -> int:
        if s=="":
            return 0
        i=0
        sign="+"
        ans=""
        n=len(s)
        while i<n and s[i]==" ":
            i+=1
        if i<n:
            if s[i]=="-" or s[i]=="+":
                sign=s[i]
                i+=1
        j=i
        while i<n:
            if s[i].isnumeric():
                ans+=s[i]
                i+=1
            else:
                break
        z=ans
        if ans.isnumeric():
            if int(sign+z)<-2147483648:
                return -2147483648
            elif int(sign+z) > 2147483647:
                return 2147483647
        if ans=="" or ans.isalpha():
            return 0
        if sign=="-":
            return int(sign+ans)
        return int(ans)