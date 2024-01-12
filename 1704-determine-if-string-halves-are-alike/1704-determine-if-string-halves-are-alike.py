class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        n=len(s)
        a,b=s[:n//2],s[n//2:]
        count1,count2=0,0
        set1=("a","e","i","o","u","A","E","I","O","U")
        for i in a:
            if i in set1:
                count1+=1
        for i in b:
            if i in set1:
                count2+=1
        return count1==count2