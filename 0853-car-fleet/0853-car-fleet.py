class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack=[]
        final=[(i,j) for i,j in zip(position,speed)]
        final=sorted(final)[::-1]
        for i,j in final:
            stack.append((target-i)/j)
            if len(stack)>=2 and stack[-1]<=stack[-2]:
                stack.pop()
        return len(stack)