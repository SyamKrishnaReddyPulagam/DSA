class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        max1=0
        a=[]
        for i in candies:
            max1=max(max1,i)
        for i in range(len(candies)):
            if (candies[i]+extraCandies)>=max1:
                a.append(True)
            else:
                a.append(False)
        return a