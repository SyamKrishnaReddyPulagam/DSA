class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        dicti={")":"(","}":"{","]":"["}
        for i in s:
            if i in dicti:
                if stack and stack[-1]==dicti[i]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)
        if stack:
            return False
        return True
    