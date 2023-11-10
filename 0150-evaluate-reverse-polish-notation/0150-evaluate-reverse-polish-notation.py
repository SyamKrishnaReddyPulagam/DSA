class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        for i in tokens:
            z=i.replace("-","")
            if z.isalnum():
                stack.append(int(i))
            else:
                u,v=stack[-1],stack[-2]
                stack.pop()
                stack.pop()
                if i=="+":
                    stack.append(u+v)
                elif i=="-":
                    stack.append(v-u)
                elif i=="*":
                    stack.append(u*v)
                else:
                    stack.append(int(v/u))
        return stack[-1]