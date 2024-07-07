class Solution:
    def getEncryptedString(self, s: str, k: int) -> str:
        dicti={i:s[i] for i in range(len(s))}
        #print(dicti)
        ans,n="",len(s)
        for i in range(len(s)):
            ans+=dicti[(i+k)%n]
        return ans