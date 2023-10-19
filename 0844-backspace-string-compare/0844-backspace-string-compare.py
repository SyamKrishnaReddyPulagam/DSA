class Solution(object):
    def backspaceCompare(self, s, t):
        stack=[]
        for i in s:
            if i=="#" and stack:
                stack.pop()
            elif i.isalpha():
                stack.append(i)
        stack1=[]
        for i in t:
            if i=="#" and stack1:
                stack1.pop()
            elif i.isalpha():
                stack1.append(i)
        print(stack,stack1)
        return "".join(stack1)=="".join(stack)