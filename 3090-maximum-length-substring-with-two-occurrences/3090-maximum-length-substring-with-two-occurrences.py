class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        n=len(s)
        i,j=0,0
        dicti,top={},0
        ans=0
        while j<n:
            if s[j] not in dicti:
                dicti[s[j]]=1
            else:
                dicti[s[j]]+=1
            top=max(top,dicti[s[j]])
            if top==3:
                ans=max(ans,j-i)
                while top==3 and i<j:
                    dicti[s[i]]-=1
                    i+=1
                    top=max(dicti.values())
            j+=1
        ans=max(ans,j-i)
        return ans