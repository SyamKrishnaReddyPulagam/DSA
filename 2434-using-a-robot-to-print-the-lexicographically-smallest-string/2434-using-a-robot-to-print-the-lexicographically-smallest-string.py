class Solution:
    def robotWithString(self, s: str) -> str:
        stack,temp=[],""
        for i in s:
            if i=="a":
                stack.append(i)
                temp+="".join(stack[::-1])
                stack=[]
            else:
                stack.append(i)
        temp+="".join(stack[::-1])
        return temp