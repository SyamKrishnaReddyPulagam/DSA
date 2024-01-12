class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        n=len(s)
        count1,count2=0,0
        for i in s[:n//2]:
            if i in ("a","e","i","o","u","A","E","I","O","U"):
                count1+=1
        for i in s[n//2:]:
            if i in ("a","e","i","o","u","A","E","I","O","U"):
                count2+=1
        return count1==count2