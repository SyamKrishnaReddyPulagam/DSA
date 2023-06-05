class Solution(object):
    def heightChecker(self, heights):
        new=[]
        x=0
        for i in heights:
            new.append(i)
        new.sort()
        for i in range(len(heights)):
            if new[i]!=heights[i]:
                x+=1
        return x