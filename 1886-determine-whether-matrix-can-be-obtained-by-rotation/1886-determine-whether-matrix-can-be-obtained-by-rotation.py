class Solution(object):
    def findRotation(self, mat, target):
        def rotate(matrix):
            start=0
            end=len(matrix)-1
            while start<end:
                matrix[start],matrix[end]=matrix[end],matrix[start]
                start+=1
                end-=1
            for i in range(len(matrix)):
                for j in range(i):
                    matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
            return matrix
        for i in range(4):
            mat=rotate(mat)
            if mat==target:
                return True
        return False