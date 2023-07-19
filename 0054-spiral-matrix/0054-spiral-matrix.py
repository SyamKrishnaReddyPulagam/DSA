class Solution(object):
    def spiralOrder(self, matrix):
        a=[]
        top,down,left,right=0,len(matrix)-1,0,len(matrix[0])-1
        while left<=right and top<=down:
            for i in range(left,right+1,1):
                a.append(matrix[top][i])
            top+=1
            for i in range(top,down+1,1):
                a.append(matrix[i][right])
            right-=1
            if top<=down:
                for i in range(right,left-1,-1):
                    a.append(matrix[down][i])
                down-=1
            if left<=right:
                for i in range(down,top-1,-1):
                    a.append(matrix[i][left])
                left+=1
        return a
    