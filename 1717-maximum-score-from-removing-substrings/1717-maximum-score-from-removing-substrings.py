class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        def func(s,cur,cost):
            stack,ans=[],0
            for i in s:
                if stack and stack[-1]==cur[0] and i==cur[1]:
                    ans+=cost
                    stack.pop()
                else:
                    stack.append(i)
            s="".join(stack)
            return s,ans
        if x>y:
            s,temp1=func(s,"ab",x)
            s,temp2=func(s,"ba",y)
            return temp1+temp2
        else:
            s,temp1=func(s,"ba",y)
            s,temp2=func(s,"ab",x)
            return temp1+temp2
            
            