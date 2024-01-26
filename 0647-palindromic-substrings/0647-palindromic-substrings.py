class Solution(object):
    def countSubstrings(self, s):
        temp=[]
        def func(s,temp):
            for i in range(len(s)):
                temp.append(s[i])
                for j in range(i+1,len(s)):
                    temp.append(s[i:j+1])
        func(s,temp)
        def func1(s):
            if s==s[::-1]:
                return True
            return False
        ans=0
        for i in range(len(temp)):
            if func1(temp[i]):
                ans+=1
        return ans