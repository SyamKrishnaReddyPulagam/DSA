class Solution(object):
    def transpose(self, matrix):
        a= [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]
        return a