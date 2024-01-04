class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        z1=Counter(ransomNote)
        z2=Counter(magazine)
        for i in z1.keys():
            if z1[i]>z2[i]:
                return False
        return True