class Solution:
    def decodeString(self, s: str) -> str:
        n=len(s)
        stack=[]
        i=0
        for i in range(n):
            if s[i]!="]":
                stack.append(s[i])
            else:
                z=""
                while stack[-1]!="[":
                    z=stack.pop()+z
                stack.pop()
                num=""
                while stack and stack[-1].isnumeric():
                    num=stack.pop()+num
                stack.append(int(num)*z)
        return "".join(stack)