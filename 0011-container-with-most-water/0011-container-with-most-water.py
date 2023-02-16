class Solution(object):
    def maxArea(self, height):
        area=0
        length=len(height)
        if length>2:
            i=0
            j=length-1
            while j>i:
                breadth=abs(i-j)
                a=min(height[i],height[j])
                b=breadth*a
                if b>area:
                    area=b
                if height[i]>height[j]:
                    j-=1
                else:
                    i+=1
        else:
            a=min(height[0],height[1])
            breadth=1
            b=breadth*a
            if b>area:
                area=b
        return area