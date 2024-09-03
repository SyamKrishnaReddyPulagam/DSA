class Solution:
    def getLucky(self, s: str, k: int) -> int:
        lower = list(string.ascii_lowercase)
        dicti={lower[i]:str(i+1) for i in range(26)}
        def gets(num):
            sums=0
            while num:
                sums+=num%10
                num=num//10
            return sums
        s=list(s)
        for i in range(len(s)):
            s[i]=dicti[s[i]]
        res="".join(s)
        res=int(res)
        for _ in range(k):
            res=gets(res)
        return res