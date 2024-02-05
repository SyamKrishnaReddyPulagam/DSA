class Solution:
    def firstUniqChar(self, s: str) -> int:
        dicti={}
        for i in range(len(s)):
            if s[i] in dicti:
                dicti[s[i]][0]+=1
            else:
                dicti[s[i]]=[1,i]
        for i in dicti:
            if dicti[i][0]==1:
                return dicti[i][1]
        return -1