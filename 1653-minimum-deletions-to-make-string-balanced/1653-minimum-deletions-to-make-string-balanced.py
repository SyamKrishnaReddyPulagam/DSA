class Solution(object):
    def minimumDeletions(self, s):
        dicti=Counter(s)
        a_to_right,b_to_left=dicti["a"],0
        print(a_to_right)
        ans=len(s)
        for i in range(len(s)):
            if s[i]=="a":
                a_to_right-=1
            ans=min(ans,a_to_right+b_to_left)
            if s[i]=="b":
                b_to_left+=1
        return ans
                