class Solution(object):
    def checkValid(self, matrix):
        for i in range(len(matrix)):
            if len(matrix[i])!=len(set(matrix[i])):
                return False
        for i in range(len(matrix)):
            for j in range(i+1,len(matrix)):
                matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]
        for i in range(len(matrix)):
            if len(matrix[i])!=len(set(matrix[i])):
                return False
        return True