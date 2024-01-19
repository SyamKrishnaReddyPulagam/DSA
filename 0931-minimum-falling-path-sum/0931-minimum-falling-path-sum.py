class Solution(object):
    def minFallingPathSum(self, matrix):
        n=len(matrix)
        temp,ans=0,float("inf")
        for row in range(1,n):
            for col in range(n):
                if col>0:
                    left=matrix[row-1][col-1]
                else:
                    left=float("inf")
                mid=matrix[row-1][col]
                if col==n-1:
                    right=float("inf")
                else:
                    right=matrix[row-1][col+1]
                matrix[row][col]=matrix[row][col]+min(left,mid,right)
        return min(matrix[-1])