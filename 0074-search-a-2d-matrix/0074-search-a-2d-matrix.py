class Solution(object):
    def searchMatrix(self, matrix, target):
        x=-1
        for i in range(len(matrix)):
            if target>=matrix[i][0]:
                x=i
        if x==-1:
            return False
        n=len(matrix[0])
        start=0
        end=n-1
        if start==end:
            return matrix[x][0]==target
        while start<=end:
            mid=(start+end)//2
            if matrix[x][mid]>target:
                end=mid-1
            elif matrix[x][mid]<target:
                start=mid+1
            else:
                return True
        return False