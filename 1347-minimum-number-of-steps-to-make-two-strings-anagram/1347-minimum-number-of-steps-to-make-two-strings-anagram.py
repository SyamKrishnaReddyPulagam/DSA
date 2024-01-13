class Solution:
    def minSteps(self, s: str, t: str) -> int:
        hash1=Counter(s)
        for i in t:
            if i in hash1:
                hash1[i]-=1
                if hash1[i]==0:
                    hash1.pop(i)
        return sum(hash1.values())