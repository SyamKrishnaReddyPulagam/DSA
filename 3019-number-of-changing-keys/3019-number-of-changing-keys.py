class Solution:
    def countKeyChanges(self, s: str) -> int:
        dicti={'A':'a','B':'b','C':'c','D':'d','E':'e','F':'f','G':'g','H':'h','I':'i','J':'j','K':'k','L':'l','M':'m','N':'n','O':'o','P':'p','Q':'q','R':'r','S':'s','T':'t','U':'u','V':'v','W':'w','X':'x','Y':'y','Z':'z'}
        n=len(s)
        i=1
        ans=0
        while i<n:
            if s[i]==s[i-1].lower() or s[i]==s[i-1].upper():
                i+=1
            else:
                ans+=1
                i+=1
        return ans