class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left,right=0,0
        dicti={}
        maxlen=0
        winlen=0
        maxele=0
        z=""
        n=len(s)
        while right<n:
            z+=s[right]
            winlen=right-left+1
            if s[right] in dicti:
                dicti[s[right]]+=1
            else:
                dicti[s[right]]=1
            maxele=dicti[max(dicti, key = dicti.get)] 
            if winlen-maxele>k:
                dicti[s[left]]-=1
                left+=1
                z=z[1:]
                winlen-=1
            maxlen=max(maxlen,winlen)
            right+=1
        return maxlen
            
                