class Solution(object):
    def generateMatrix(self, n):
        a=[[0 for i in range(n)]for i in range(n)]
        left,right,top,down=0,n-1,0,n-1
        temp=1
        while left<=right and top<=down:
            for i in range(left,right+1,1):
                a[top][i]=temp
                temp+=1
            top+=1
            for i in range(top,down+1,1):
                a[i][right]=temp
                temp+=1
            right-=1
            if top<=down:
                for i in range(right,left-1,-1):
                    a[down][i]=temp
                    temp+=1
                down-=1
            if left<=right:
                for i in range(down,top-1,-1):
                    a[i][left]=temp
                    temp+=1
                left+=1
        return a