class Solution(object):
    def heightChecker(self, heights):
        """x=0
        i=0
        while i<len(heights):
            while heights[i]!=sorted(heights)[i]:
                x+=1
            i+=1
        return x"""
        sort_heights = sorted(heights)
        return sum([0 if heights[i] == sort_heights[i] else 1 for i in range(len(heights))])