class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1=len(s1)
        n2=len(s2)
        if n1>n2:
            return False
        if n1==n2:
            return sorted(s1)==sorted(s2)
        from collections import OrderedDict
        i=0
        dicti1=collections.Counter(s1)
        dicti1=OrderedDict(sorted(dicti1.items()))
        while i<=n2-n1:
            j=i+n1
            z=s2[i:j]
            z=Counter(z)
            dicti2=OrderedDict(sorted(z.items()))
            if dicti1==dicti2:
                return True
            i+=1
        return False