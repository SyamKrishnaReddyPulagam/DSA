class Solution:
    def compress(self, chars: List[str]) -> int:
        i=0
        s=""
        while i<len(chars):
            j=i+1
            while j<len(chars) and chars[i]==chars[j]:
                j+=1
            s+=chars[i]
            if j-i>1:
                s+=str(j-i)
            i=j
        chars.clear()
        chars.extend(s)
        return len(chars)